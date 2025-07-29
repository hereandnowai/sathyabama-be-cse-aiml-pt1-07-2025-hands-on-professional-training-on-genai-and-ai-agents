import os # Import the os module for interacting with the operating system
from openai import OpenAI # Import the OpenAI library for API interaction
from dotenv import load_dotenv # Import load_dotenv to load environment variables
import requests # Import requests for making HTTP requests

# Load environment variables from the .env file
load_dotenv()

# Get the Google API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
# Raise an error if the API key is not found
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not found.")

# Initialize the OpenAI client with the base URL and API key
client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai", api_key=api_key)

# Define the URL for the text context file on GitHub
url = "https://raw.githubusercontent.com/hereandnowai/vac/refs/heads/master/prospectus-context.txt"
# Make an HTTP GET request to fetch the content
response = requests.get(url)

# Determine the script's directory and define the local file path for saving the text
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "profile-of-hereandnowai.txt")
# Write the fetched content to the local file
with open(file_path, "wb") as f:
    f.write(response.content)