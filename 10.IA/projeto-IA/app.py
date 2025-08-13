from flask import Flask, request, jsonify, render_template
import requests
import os

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Sua chave aqui (segura enquanto for local)
API_KEY = os.getenv("OPEN_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perguntar', methods=['POST'])
def perguntar():
    data = request.json
    pergunta = data.get("pergunta")

    if not pergunta:
        return jsonify({"erro": "Pergunta não recebida"}), 400

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": pergunta}]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        resposta_json = response.json()
        conteudo = resposta_json["choices"][0]["message"]["content"]
        return jsonify({"resposta": conteudo})
    
    else:
        return jsonify({"erro": "Erro na API", "status": response.status_code, "mensagem": response.text}), 500

if __name__ == '__main__':
    app.run(debug=True)