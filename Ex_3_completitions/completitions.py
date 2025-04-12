import requests
import os
from dotenv import load_dotenv

#API Key
load_dotenv()
api_key = os.getenv('API_KEY')

# Endpoint delle API
url = "https://api.openai.com/v1/chat/completions"

# La domanda da inviare
user_question = input("Scrivi la tua domanda: ")

# Corpo della richiesta
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "Sei un assistente utile."},
        {"role": "user", "content": user_question}
    ],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

# Stampa la risposta del modello
if response.status_code == 200:
    reply = response.json()["choices"][0]["message"]["content"]
    print("Risposta:", reply)
else:
    print("Errore:", response.status_code, response.text)
