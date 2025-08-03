🤖 Gemini Chatbot (Google Generative AI)
This is a simple terminal-based chatbot built using the Gemini API (`gemini-2.0-flash` model). It allows you to interact with Google's Generative AI through your terminal using Python.

🚀 Features
- Uses Google Generative AI (`gemini-2.0-flash`)
- Interactive terminal chatbot
- Clean `.env`-based API key setup
- Easy to run and modify
🛠️ Setup Instructions

1. Clone the Repository
    git clone: https://github.com/SHIVAKUMARJATLA/Gemini-Chatbot.git

    cd Gemini-Chatbot


2. Install Dependencies
    pip install -r requirements.txt
    requirements.txt
    google-generativeai
    python-dotenv

3. Set Your API Key
    Create a `.env` file in the root directory and add your Gemini API key:

    API_KEY=your_api_key_here

4. Run the Chatbot

    python gemini_chatbot.py

    Type your message and press Enter. Type `exit` to quit the chatbot.


🤖 Chat with Gemini! Type 'exit' to quit.

    You: Hello Gemini!
    Gemini: Hello! How can I assist you today?

    You: Tell me a joke
    Gemini: Why don't scientists trust atoms? Because they make up everything!

    You: exit
    👋 Exiting chat. Goodbye!

