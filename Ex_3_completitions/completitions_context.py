import requests
import os

# API Key
from dotenv import load_dotenv

#API Key
load_dotenv()
api_key = os.getenv('API_KEY')

# Endpoint delle API
url = "https://api.openai.com/v1/chat/completions"

def get_contextual_answer(text, question):

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Testo: " + text + "\nDomanda: " + question}
    ]
    # Corpo della richiesta
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    # Stampa la risposta del modello
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    else:
        return f"Errore: {response.status_code}, {response.text}"

text = "Albert Einstein è stato un fisico tedesco di origini ebraiche, noto per aver sviluppato la teoria della relatività."
question = "Chi era Albert Einstein?"

answer = get_contextual_answer(text, question)
print("Risposta:", answer)