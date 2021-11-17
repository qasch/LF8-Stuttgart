from flask import Flask, render_template

# Flask Objekt erzeugen
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test/<my_name>")
def test(my_name):
    return render_template("test.html", my_name=my_name)


# 'Main Methode', Startpunkt der Applikation
if __name__ == '__main__':
    app.run(debug=True)
