#llm.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def call_llm(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1   # très important pour les agents
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]


