import pika
from flask import Flask, jsonify

app = Flask(__name__)
messages = []

def callback(ch, method, properties, body):
    messages.append(body.decode())
    print(f" [x] Received {body.decode()}")

def receive_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='hello_world')
    channel.basic_consume(queue='hello_world', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    from threading import Thread
    thread = Thread(target=receive_messages)
    thread.start()
    app.run(host='0.0.0.0', port=5000)
