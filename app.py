from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Ich bin eine richtig echte kleine Flask App"

if __name__ == '__main__':
    app.run()
