from flask import Flask, render_template

# Flask Objekt erzeugen
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")


# 'Main Methode', Startpunkt der Applikation
if __name__ == '__main__':
    app.run(debug=True)
