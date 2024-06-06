import time
import random
import requests

def broadcast_message():
    while True:
        interval = random.randint(1, 10)
        time.sleep(interval)
        requests.post('http://hello-receiver-service:5001/receive', json={"message": "Hello world"})

if __name__ == "__main__":
    broadcast_message()
