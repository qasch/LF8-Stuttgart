from flask import Flask, render_template, request
from markupsafe import escape
import sqlite3

# Flask Objekt erzeugen
app = Flask(__name__)


@app.route("/")
def index():
    # Verbindung zur Datenbank herstellen
    connection = sqlite3.connect('db/flask.db')
    # Cursor erzeugen
    cursor = connection.cursor()

    # Cursor kann beliebige SQL Anweisungen ausführen
    result = cursor.execute("SELECT * FROM person").fetchall()

    return render_template("index.html", result=result)


# Wir können auch mehrere Routen für eine Funktion
# angeben und zusätzlich Default Werte für Parameter
# festlegen
@app.route("/test/", defaults={'dest_url': None})
@app.route("/test/<string:dest_url>/<from_url>")
def test(dest_url, from_url):
    return render_template("test.html", dest_url=escape(dest_url), from_url=from_url)


@app.route('/form/')
def form():
    return render_template("form.html")


# TODO: Check methods
@app.route('/results/', methods=['POST'])
def results():
    # mit request.args.get() erhält man nur GET Paramenter
    #vorname = request.args.get('vorname')
    # mit request.form.get() erhält man die POST Daten
    vorname = request.form.get('vorname')
    passwort = request.form.get('passwort')
    # Prüfung, ob email eingetragen wurde, ansonten Fehler ausgeben
    if request.form.get('email'):
        email = request.form.get('email')
    else:
        email = "Not provided"

    # Verbindung zur Datenbank herstellen
    connection = sqlite3.connect('db/flask.db')
    # Cursor erzeugen
    cursor = connection.cursor()

    # Cursor kann beliebige SQL Anweisungen ausführen
    cursor.execute(
        # F-String (Im Zusammenspiel mit SQL wäre Parameterization der bessere Weg)
        f"""INSERT INTO person
        (
            vorname,
            passwort,
            email
        )
        VALUES (
            '{vorname}',
            '{passwort}',
            '{email}'
            )
        """)

    connection.commit()
    connection.close()

    return render_template("results.html", vorname=vorname, passwort=passwort)


# 'Main Methode', Startpunkt der Applikation
if __name__ == '__main__':
    app.run(debug=True)
