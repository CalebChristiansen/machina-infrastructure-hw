from flask import Flask, request
import datetime

app = Flask(__name__)
messages = []

@app.route('/receive', methods=['POST'])
def receive_message():
    content = request.json
    message = {
        "text": content["message"],
        "timestamp": datetime.datetime.now().isoformat()
    }
    messages.append(message)
    return '', 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return {"messages": messages}, 200

@app.route('/messages/since', methods=['GET'])
def get_messages_since():
    timestamp = request.args.get('timestamp')
    if not timestamp:
        return {"messages": messages}, 200

    filtered_messages = [msg for msg in messages if msg['timestamp'] > timestamp]
    return {"messages": filtered_messages}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
