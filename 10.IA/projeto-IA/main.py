from flask import Flask, request, jsonify, render_template
import requests
import os 
from dotenv import load_dotenv

load_dotenv()



# SUA CHAVE AQUI (substitua por uma chave nova e válida do OpenRouter)
API_KEY = os.getenv("OPEN_API_KEY")


# Endpoint da OpenRouter
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Cabeçalhos obrigatórios
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:5000"  # OU o domínio que você usou na chave
}

# Corpo da requisição (prompt)
data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Como fazer uma pizza?"}
    ]
}

# Envio da requisição
response = requests.post(API_URL, headers=headers, json=data)

# Verificação da resposta
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    resposta_json = response.json()
    conteudo = resposta_json["choices"][0]["message"]["content"]
    print("Resposta da IA:\n", conteudo)
else:
    print("Erro na requisição:")
    print(response.text)
