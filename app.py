from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Hello from Flask app deployed via Jenkins to EC2!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
