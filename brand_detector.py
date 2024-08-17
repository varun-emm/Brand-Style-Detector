import os
from openai import OpenAI
from dotenv import load_dotenv
import asyncio
from pyppeteer import launch
import requests
from getpass import getpass

# Load environment variables from a .env file
load_dotenv()

# Set environment variables if not already set
def set_env_var(var_name: str):
    if not os.getenv(var_name):
        os.environ[var_name] = getpass(f"Please enter {var_name}: ")

# Configure and check required environment variables
REQUIRED_ENV_VARS = ["OPENAI_API_KEY"]
for var in REQUIRED_ENV_VARS:
    set_env_var(var)

# Initialize OpenAI client
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

async def take_screenshot(url: str, output_file: str) -> None:
    """Take a screenshot of the given URL and save it to the specified file."""
    try:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        await page.screenshot({'path': output_file})
    finally:
        await browser.close()

def upload_to_0x0(file_path: str) -> str:
    """Upload a file to 0x0.st and return the download link."""
    with open(file_path, 'rb') as file:
        response = requests.post('https://0x0.st', files={'file': file})
        response.raise_for_status()
        return response.text.strip()

def analyze_screenshot(file_link: str) -> str:
    """Analyze the screenshot using the OpenAI API."""
    try:
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": "What does the company do, what is their name, primary color, secondary color, primary font, secondary font, and overall design of the brand?"},
                {
                "type": "image_url",
                "image_url": {
                    "url": file_link,
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Failed to analyze screenshot: {e}")

def main():
    # URL of the page to take a screenshot of
    url = 'https://www.imedfurns.com/'
    # Output file name for the screenshot
    output_file = 'screenshot_page1.png'

    # Run the async function to take the screenshot
    asyncio.get_event_loop().run_until_complete(take_screenshot(url, output_file))

    # Upload the screenshot to 0x0.st and get the file link
    file_link = upload_to_0x0(output_file)
    print(f"Screenshot uploaded. File link: {file_link}")

    # Analyze the screenshot using OpenAI API
    analysis_result = analyze_screenshot(file_link)
    print("Website analysis result:")
    print(analysis_result)

if __name__ == "__main__":
    main()
