from dotenv import load_dotenv
import os
import json
import openai
import requests

# Load environment variables from .env file
load_dotenv()

# Set up GitHub and OpenAI API credentials & variables
username = 'dhrubasaha08'

repo_owner = 'dhrubasaha08'
repo = 'Discuss-Bot'

model = 'gpt-3.5-turbo'

discussion_arr = 1  # Number of discussions to fetch

access_token = os.getenv("API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to generate a concise solution using OpenAI API
def generate_solution(title, body):
    """
    Generates a concise solution for a given problem using OpenAI API.

    Args:
        title (str): The title of the problem.
        body (str): The body/description of the problem.

    Returns:
        str: The generated concise solution.
    """
    content = f"User on GitHub community discussion having a problem, generate a possible concise solution, the problem -\n{title}\n{body}"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content}
        ],
        max_tokens=100,
        temperature=0.6,
        n=1
    )
    generated_solution = response.choices[0].message.content.strip()
    return generated_solution


# GraphQL query to fetch discussions
query = '''
query($owner: String!, $repo: String!, $first: Int!) {
  repository(owner: $owner, name: $repo) {
    discussions(first: $first) {
      totalCount
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        id
        title
        body
        author {
          login
        }
        comments(first: 1) {
          nodes {
            author {
              login
            }
            body
          }
        }
      }
    }
  }
}
'''

# GraphQL mutation to add a comment
mutation = '''
mutation($discussionId: ID!, $body: String!) {
  addDiscussionComment(input: {discussionId: $discussionId, body: $body}) {
    comment {
      id
    }
  }
}
'''

# Variables for the GraphQL queries/mutations
variables = {
    'owner': repo_owner,
    'repo': repo,
    'first': discussion_arr
}

# Construct the request headers
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Send the GraphQL request to fetch discussions
response = requests.post('https://api.github.com/graphql',
                         json={'query': query, 'variables': variables}, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Extract discussions from the response
    discussions = data['data']['repository']['discussions']['nodes']

    # Loop through each discussion
    for discussion in discussions:
        title = discussion['title']
        author = discussion['author']['login']
        comments = discussion['comments']['nodes']

        # Check if a response has already been provided
        if comments:
            existing_comment_author = comments[0]['author']['login']

            # If a response has been provided, skip to the next discussion
            if existing_comment_author != username:
                continue

        # Generate a concise solution using OpenAI API
        concise_solution = generate_solution(title, discussion['body'])

        # Construct the response body with the bot tag and warning
        response_body = f"Hey, @{author} {concise_solution} \n\nNote: This is an automated response. Please review and verify the solution. `@{username} [BOT]`"

        # Get the discussion ID
        discussion_id = discussion['id']

        # Send the GraphQL mutation to add a comment
        response = requests.post('https://api.github.com/graphql', json={'query': mutation, 'variables': {
                                 'discussionId': discussion_id, 'body': response_body}}, headers=headers)

        # Check if the mutation request was successful
        if response.status_code == 200:
            response_data = response.json()
            comment_id = response_data['data']['addDiscussionComment']['comment']['id']
            print(
                f"Successfully replied to discussion: {title} (Comment ID: {comment_id})")
        else:
            print(f"Failed to add comment to discussion: {title}")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
