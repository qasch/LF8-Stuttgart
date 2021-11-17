from flask import Flask, render_template
from markupsafe import escape

# Flask Objekt erzeugen
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


# Wir können auch mehrere Routen für eine Funktion
# angeben und zusätzlich Default Werte für Parameter
# festlegen
@app.route("/test/", defaults={'dest_url': None})
@app.route("/test/<string:dest_url>/<from_url>")
def test(dest_url, from_url):
    return render_template("test.html", dest_url=escape(dest_url), from_url=from_url)


# 'Main Methode', Startpunkt der Applikation
if __name__ == '__main__':
    app.run(debug=True)
