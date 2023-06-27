# Discuss Bot
This repository contains a Python-based auto-response bot that leverages the GitHub API and OpenAI's language model to automatically generate responses to discussions on GitHub. The bot monitors GitHub repository discussions and provides concise solutions to problems posted by users. The bot utilizes the GitHub API to fetch discussions from a specified repository and OpenAI's GPT-3.5 Turbo model to generate helpful responses. It identifies discussions  and adds a generated solution as a comment.


## Features
- Seamless integration with the GitHub repository discussion tab.
- Advanced natural language processing (NLP) for enhanced understanding and response generation.
- Monitors GitHub repository discussions
- Generates concise solutions using OpenAI's GPT-3.5 Turbo language model
- Automatically adds generated solutions as comments to discussions
- Supports customization through environment variables and GraphQL queries/mutations

### Usage
- Set up your GitHub and OpenAI API credentials in the environment variables.
- Configure the repository details, API URL, and access token in the code.
- Refer to the `.env.example` file to see the required variables.


## Setup
- Clone the repository:
  ```shell
  git clone https://github.com/dhrubasaha08/Discuss-Bot.git
  cd Discuss-Bot
  ```

- Install the dependencies:
  ```shell
  pip install -r requirements.txt
  ```

- Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add the following lines to the `.env` file and replace the placeholder values with your actual credentials:
  ```plaintext
  API_KEY=<github_api_key>
  OPENAI_API_KEY=<open_ai_key>
  ```

- Start the DiscussBot:
  ```shell
  python main.py
  ```


## File Structure
```
/.github/workflows/auto_response.yml
/.env
/.gitignore
/LICENSE
/main.py
/README.md
/requirements.txt
```


## Dependencies
[![GitHub](https://img.shields.io/github/pipenv/locked/dependency-version/dhrubasaha08/discuss-bot/openai?style=flat-square)](https://github.com/dhrubasaha08/discuss-bot/blob/main/requirements.txt)

The following dependencies are required to run Discuss Bot:
- `Python` (3.10 or higher)
  - `dotenv` (0.19.1 or higher)
  - `requests` (2.26.0 or higher)
  - `openai` (0.27.0 or higher)

## License
DiscussBot is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as per the terms of the license.


## Contributing
Contributions are welcome and encouraged! If you'd like to contribute to DiscussBot, please follow these steps:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and ensure that the code passes all tests.
- Commit your changes and push them to your forked repository.
- Submit a pull request with a detailed description of your changes.
Please adhere to the code style guidelines and maintain clear commit messages to help with the review process.


## Acknowledgements
DiscussBot is built upon the powerful capabilities of OpenAI's natural language processing. We extend our gratitude to the entire OpenAI community for their valuable contributions.


## Contact
If you have any questions, suggestions, or feedback, please reach out to me at [@dhrubasaha08](https://github.com/dhrubasaha08/).
