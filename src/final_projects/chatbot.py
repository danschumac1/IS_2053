import openai
import json
import getpass

# Load prompts
with open('prompts.json', 'r') as f:
    prompts_data = json.load(f)

system_prompt = prompts_data['system_prompt']
few_shot_examples = prompts_data['few_shot_examples']
chat_history = []

def generate_response(user_input):
    messages = [{'role': 'system', 'content': system_prompt}] + few_shot_examples + chat_history
    messages.append({'role': 'user', 'content': user_input})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    reply = response['choices'][0]['message']['content']
    return reply

def save_chat_history(filepath):
    with open(filepath, 'w') as f:
        json.dump(chat_history, f, indent=4)

def main():
    print("Welcome to the Assistant ChatBot! Type 'exit' or 'quit' to end.")
    openai.api_key = getpass.getpass("Please paste your OpenAI API key (input hidden): ")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        reply = generate_response(user_input)
        chat_history.append({'role': 'user', 'content': user_input})
        chat_history.append({'role': 'assistant', 'content': reply})

        print(f"Bot: {reply}")

    save_chat_history('chat_history.json')
    print("Chat history saved to 'chat_history.json'. Goodbye!")

if __name__ == "__main__":
    main()
