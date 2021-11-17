from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Ich bin eine Flask App"

