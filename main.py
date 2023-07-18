from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar las preguntas del usuario
@app.route('/ask', methods=['POST'])
def ask_question():
    user_message = request.form['user_message']

    # Llamada al API de ChatGPT
    api_key = 'TU_API_KEY'  # Reemplaza con tu API key de ChatGPT
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': user_message}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    chatbot_reply = response.json()['choices'][0]['message']['content']
    return jsonify({'reply': chatbot_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0')