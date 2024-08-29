from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import os
from dotenv import load_dotenv
from models import db, Address, User, Promise, PersonalDetail, Payment, Loan, LoanApplication

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slack_bot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Vincular SQLAlchemy con la aplicación Flask
db.init_app(app)

# Claves API cargadas desde variables de entorno
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Inicializa la base de datos
with app.app_context():
    db.create_all()

# Función para enviar mensajes a Slack
def send_message(channel, text):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Authorization': f'Bearer {SLACK_BOT_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'channel': channel,
        'text': text
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        print(f"Error enviando mensaje a Slack: {response.status_code}, {response.text}")

# Función para consultar la API de OpenAI
def query_openai(prompt):
    expert_prompt = """
    Eres un experto en bases de datos SQL. Los usuarios pueden hacerte preguntas sobre cómo hacer consultas SQL sobre una base de datos que contiene las siguientes tablas:
    
    1. `addresses` - Información de direcciones.
    2. `users` - Información de usuarios, incluyendo identificadores únicos, detalles personales, y más.
    3. `promises` - Información sobre promesas de pago.
    4. `personal_details` - Detalles personales como dependientes, nivel educativo, etc.
    5. `payments` - Información sobre pagos realizados.
    6. `loans` - Información de préstamos.
    7. `loan_applications` - Información sobre aplicaciones de préstamos.

    Siempre explica la lógica detrás de las consultas SQL que propones, y considera la seguridad de la base de datos y la eficiencia de las consultas.
    
    Pregunta del usuario: {}
    """

    full_prompt = expert_prompt.format(prompt)
    
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{"role": "user", "content": full_prompt}],
        'max_tokens': 150
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error llamando a la API de OpenAI: {response.status_code}, {response.text}")
        return None

# Ruta para manejar eventos de Slack
@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.json

    # Verificación de URL de Slack
    if 'type' in data and data['type'] == 'url_verification':
        return jsonify({'challenge': data['challenge']})

    # Manejo de eventos de mensajes
    if 'event' in data:
        event = data['event']
        if event.get('type') == 'message' and not event.get('bot_id'):
            user_message = event.get('text')
            channel = event.get('channel')

            # Verificación del mensaje recibido
            print(f"Mensaje recibido: {user_message} en el canal {channel}")

            # Llamar a la API de OpenAI para obtener una respuesta
            response = query_openai(user_message)

            if response:
                bot_response = response['choices'][0]['message']['content'].strip()

                # Almacenar en la base de datos (ejemplo si quieres guardar mensajes)
                # message_record = Message(user_message=user_message, bot_response=bot_response)
                # db.session.add(message_record)
                # db.session.commit()

                # Enviar respuesta a Slack
                send_message(channel, bot_response)
            else:
                send_message(channel, "Lo siento, hubo un problema al procesar tu solicitud.")

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
