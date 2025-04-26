import requests
import os
import json
from dotenv import load_dotenv
import wikipedia


load_dotenv()
api_key = os.getenv('API_KEY')
URL = os.getenv('completition.url')
model_version = os.getenv('completition.nodel.v1')


headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def wikipedia_summary(query):
    """Restituisce un riassunto da Wikipedia."""
    try:
        summary = wikipedia.summary(query, sentences=2)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}


functions = [
    {
        "name": "wikipedia_summary",
        "description": "Restituisce un riassunto da Wikipedia.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Argomento da cercare su Wikipedia"
                }
            },
            "required": ["query"]
        }
    }
]

user_question = input("Scrivi il termine per il riassunto su Wikipedia: ")

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

        if function_name == "wikipedia_summary":
            result = wikipedia_summary(**function_args)
            print(f"Riassunto: {result}")
        else:
            print(f"Function {function_name} non gestita.")
    else:
        print("Risposta:", message["content"])

else:
    print("Errore:", response.status_code, response.text)
