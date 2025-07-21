'''
2025-07-21
Author: Dan Schumacher
How to run:
   python .\src\final_projects\chat_bot_getting_started.py
'''

from openai import OpenAI
import getpass

# === Setup ===
system_prompt = "You are a helpful assistant."

def generate_response(user_input, client):
    """Send the user input and chat history to the model and return its reply."""
    messages = [{'role': 'system', 'content': system_prompt}]
    messages.append({'role': 'user', 'content': user_input})

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages
    )
    reply = response.choices[0].message.content
    return reply

def main():
    api_key = getpass.getpass("Enter your OpenAI API key: ")
    client = OpenAI(api_key=api_key)

    message = "Whats the capital of spain?"

    reply = generate_response(message, client)
    print(f"Bot: {reply}")

if __name__ == "__main__":
    main()
