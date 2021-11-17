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
@app.route("/test/", defaults={'my_name': None})
@app.route("/test/<string:my_name>")
def test(my_name):
    sum = my_name * 2
    return render_template("test.html", my_name=escape(my_name))


# 'Main Methode', Startpunkt der Applikation
if __name__ == '__main__':
    app.run(debug=True)
