from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        response = requests.get('http://hello-receiver-service:5001/messages')
        response.raise_for_status()  # Ensure we raise an exception for HTTP errors
        messages = response.json().get('messages', [])
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}", 500
    return render_template_string("""
    <!doctype html>
    <html>
    <head><title>Hello World Broadcasts</title></head>
    <body>
        <h1>Hello World Broadcasts</h1>
        <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    """, messages=messages)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
