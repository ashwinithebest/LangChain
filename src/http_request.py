import os
import requests
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())  # read local .env file

# Set environment variables
endpoint = os.getenv("OPENAI_ENDPOINT")
api_key = os.getenv("OPENAI_API_KEY")

# Define headers for the request
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

# Function to get completion from Azure OpenAI
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0, max_tokens=50):
    url = endpoint
    data = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
        return None
