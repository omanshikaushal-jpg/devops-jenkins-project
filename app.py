from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hey Team!! DevOps Pipeline v2.0 is Live & Automated! </h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)