import requests
import os
import json
from dotenv import load_dotenv

# Carica le variabili d'ambiente
load_dotenv()
api_key = os.getenv('API_KEY')
URL = os.getenv('completition.url')
model_version = os.getenv('completition.model.v1')

# Headers API
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def calculate(expression):
    """Valuta un'espressione matematica."""
    try:
        result = eval(expression)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
    
functions = [
    {
        "name": "calculate",
        "description": "Valuta un'espressione matematica.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Espressione matematica da valutare, es: '2 + 3 * 4'"
                }
            },
            "required": ["expression"]
        }
    }
]

user_question = input("Scrivi la tua domanda: ")

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

response = requests.post(URL, headers=headers, json=data)

if response.status_code == 200:
    res_json = response.json()
    message = res_json["choices"][0]["message"]

    if message.get("function_call"):
        # Function call individuata
        function_name = message["function_call"]["name"]
        function_args = json.loads(message["function_call"]["arguments"])

        if function_name == "calculate":
            result = calculate(**function_args)
            print(f"Risultato: {result}")
        else:
            print(f"Function {function_name} non gestita.")
    else:
        print("Risposta:", message["content"])

else:
    print("Errore:", response.status_code, response.text)