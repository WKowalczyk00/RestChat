from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage (replace with DB in production)
messages = []

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def send_message():
    data = request.json
    message = {
        'user': data.get('user'),
        'text': data.get('text'),
        'timestamp': datetime.utcnow().isoformat()
    }
    messages.append(message)
    return jsonify(message), 201

if __name__ == '__main__':
    app.run(debug=True)
