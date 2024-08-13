from dotenv import load_dotenv, find_dotenv
from http_request import get_completion
from langchain_openai import AzureChatOpenAI
import os

# Load environment variables from .env file
load_dotenv(find_dotenv()) 

# Set environment variables
endpoint = os.getenv("OPENAI_ENDPOINT")
api_key = os.getenv("OPENAI_API_KEY")
os.environ["AZURE_OPENAI_API_KEY"] = api_key
os.environ["AZURE_OPENAI_ENDPOINT"] =endpoint 


llm = AzureChatOpenAI(
    azure_deployment="gpt-35-turbo", 
    api_version="2024-04-01-preview", 
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
   
)
messages = [
    (
        "system",
        "You are a helpful assistant.",
    ),
    ("human", "who won last IPL "),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)

# Example usage
# response = get_completion("tell me table of 5")
# print(response)
