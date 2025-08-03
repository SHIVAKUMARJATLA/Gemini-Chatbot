# Load environment variables from .env file
from dotenv import load_dotenv
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the .env file
dotenv_path = os.path.join(script_dir, '.env')

# Load environment variables
load_dotenv(dotenv_path)

# Import the Gemini API library
import google.generativeai as genai

# Get the API key from the environment variables
API_KEY = os.getenv('API_KEY')

# Configure the Gemini model with your API key
genai.configure(api_key=API_KEY)

# Initialize the Gemini generative model (flash version)
model = genai.GenerativeModel("gemini-2.0-flash")

# Start a chat session
chat = model.start_chat()

print("🤖 Chat with Gemini! Type 'exit' to quit.\n")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("👋 Exiting chat. Goodbye!")
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
