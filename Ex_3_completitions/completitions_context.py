import requests
import os

# API Key
from dotenv import load_dotenv

#API Key
load_dotenv()
api_key = os.getenv('API_KEY')
URL = os.getenv('completition.url')
model_version=os.getenv('completition.nodel.v2')
# Endpoint delle API
url = URL

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
        "model": model_version,
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