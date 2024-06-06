import time
import random
import pika

def broadcast_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='hello_world')

    while True:
        message = "Hello world"
        channel.basic_publish(exchange='', routing_key='hello_world', body=message)
        print(f" [x] Sent {message}")
        time.sleep(random.randint(1, 10))

    connection.close()

if __name__ == "__main__":
    broadcast_message()
