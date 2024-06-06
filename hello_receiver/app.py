from flask import Flask, request

app = Flask(__name__)
messages = []

@app.route('/receive', methods=['POST'])
def receive_message():
    content = request.json
    messages.append(content["message"])
    return '', 200

@app.route('/messages', methods=['GET'])
def get_messages():
    return {"messages": messages}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
