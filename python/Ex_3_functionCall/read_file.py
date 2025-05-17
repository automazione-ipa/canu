import requests
import os
import json
from dotenv import load_dotenv

# Carica le variabili d'ambiente
load_dotenv()
api_key = os.getenv('API_KEY')
URL = os.getenv('completition.url')
model_version = os.getenv('completition.nodel.v1')

# Headers API
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def read_file(file_name):
    """Legge un file e restituisce il contenuto."""
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return {"content": f.read()}
    except FileNotFoundError:
        return {"error": f"File non trovato: {file_name}"}
    except Exception as e:
        return {"error": str(e)}

# --- JSON Schema per function-calling ---
functions = [
    {
        "name": "read_file",
        "description": "Legge un file e restituisce il contenuto.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "Percorso del file da leggere"
                }
            },
            "required": ["file_name"]
        }
    }
]

# Interazione utente
user_question = input("Scrivi il nome del file da leggere: ")

data = {
    "model": model_version,
    "messages": [
        {"role": "system", "content": "Sei un assistente utile."},
        {"role": "user", "content": user_question}
    ],
    "functions": functions,
    "function_call": "auto",
    "temperature": 0.7
}

# Invio richiesta
response = requests.post(URL, headers=headers, json=data)

# Gestione risposta
if response.status_code == 200:
    res_json = response.json()
    message = res_json["choices"][0]["message"]

    if message.get("function_call"):
        # Function call individuata
        function_name = message["function_call"]["name"]
        function_args = json.loads(message["function_call"]["arguments"])

        if function_name == "read_file":
            result = read_file(**function_args)
            print(f"Contenuto del file: {result}")
        else:
            print(f"Function {function_name} non gestita.")
    else:
        print("Risposta:", message["content"])

else:
    print("Errore:", response.status_code, response.text)
