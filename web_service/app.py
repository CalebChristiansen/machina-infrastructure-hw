from flask import Flask, render_template_string, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <!doctype html>
    <html>
    <head>
        <title>Hello World Broadcasts</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    </head>
    <body>
        <div class="container">
            <h1 class="my-4">Hello World Broadcasts</h1>
            <div id="messages" class="row">
                <!-- Messages will be dynamically added here -->
            </div>
        </div>

        <script>
            let lastTimestamp = null;

            function fetchMessages() {
                $.ajax({
                    url: '/messages-since',
                    method: 'GET',
                    data: {timestamp: lastTimestamp},
                    success: function(data) {
                        data.messages.forEach(function(message) {
                            $('#messages').prepend(`
                                <div class="col-md-4 mb-3">
                                    <div class="card">
                                        <div class="card-body">
                                            <h5 class="card-title">${message.text}</h5>
                                            <p class="card-text"><small class="text-muted">${new Date(message.timestamp).toLocaleString()}</small></p>
                                        </div>
                                    </div>
                                </div>
                            `);
                            lastTimestamp = message.timestamp;
                        });
                    }
                });
            }

            $(document).ready(function() {
                setInterval(fetchMessages, 1000); // Fetch new messages every 1 second
            });
        </script>
    </body>
    </html>
    """)

@app.route('/messages-since', methods=['GET'])
def get_messages_since():
    timestamp = request.args.get('timestamp')
    try:
        response = requests.get(f'http://hello-receiver-service:5001/messages/since?timestamp={timestamp}')
        response.raise_for_status()  # Ensure we raise an exception for HTTP errors
        messages = response.json().get('messages', [])
        return jsonify(messages=messages)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
