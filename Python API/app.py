from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Cloud Native Python App</h1><p>Status: Running</p>"

@app.route('/health')
def health():
    return jsonify(
        status="up",
        cloud="aws",
        containerized=False
    )

if __name__ == '__main__':
    # Run explicitly on 0.0.0.0 so we can access it externally later
    app.run(host='0.0.0.0', port=5001)
