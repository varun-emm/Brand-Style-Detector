# Website Screenshot and Analysis Tool

This project is a Python-based tool designed to analyse websites, to extract branding information such as company name, primary and secondary colors, fonts, and overall design.



## Requirements

- Python 3.7+
- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- [0x0.st](https://0x0.st) for file hosting
- The following Python packages:
  - `openai`
  - `python-dotenv`
  - `pyppeteer`
  - `requests`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/website-screenshot-analysis.git
   cd website-screenshot-analysis

Create a .env file in the root of your project directory and add your OpenAI API key in the following format:

OPENAI_API_KEY = "Input_your_key_here"