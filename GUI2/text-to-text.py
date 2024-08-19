from groq import Groq
from datetime import datetime
import os

# Initialize Groq API client with the key set as an environment variable
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_prompt(prompt, text):
    # Create a conversation structure for the prompt
    convo = [{'role': 'user', 'content': prompt}]
    chat_completion = groq_client.chat.completions.create(messages=convo, model='llama3-70b-8192')
    response = chat_completion.choices[0].message

    # Print the time of the save
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save the conversation to history.txt
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"=== Conversation at {timestamp} ===\n")
        file.write(f"USER: {text}\n")
        file.write(f"ASSISTANT: {response.content}\n")
        file.write(f"____________________________________________________________________________\n\n")

    # Print the response from the AI
    print(f"{response.content}")
    return response.content

def translate_text(text, language):
    # Prompt for translation
    prompt = f"Translate the following to {language}: {text}"
    response = groq_prompt(prompt, text)
    return response

if __name__ == "__main__":
    # Ask for target language and text to translate
    language = input("Enter Target Language: ")
    prompt = input('Enter text to translate: ')

    # Translate the text and display the result
    response = translate_text(prompt, language)
