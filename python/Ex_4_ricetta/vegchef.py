import requests
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('ollama.url')
def genera_ricetta(ingrediente, modello="vegchef"):
    url = URL


    prompt = f"Dammi una ricetta vegana semplice con {ingrediente} come ingrediente principale."

    payload = {
        "model": modello,
        "prompt": prompt,
        "stream": False  # disabilita lo streaming, ricevi tutto in un colpo
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    print("✅ Risposta generata:")
    print(data["response"])

if __name__ == "__main__":
    ingrediente = input("Inserisci un ingrediente: ")
    genera_ricetta(ingrediente)