import requests
import os
from dotenv import load_dotenv

#API Key
load_dotenv()
api_key = os.getenv('API_KEY')
URL = os.getenv('completition.url')
model_version=os.getenv('completition.nodel.v1')
# Endpoint delle API
url = URL

# La domanda da inviare
user_question = input("Scrivi la tua domanda: ")

# Corpo della richiesta
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": model_version,
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
