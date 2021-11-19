import sqlite3


# Verbindung zur Datenbank herstellen
connection = sqlite3.connect('db/flask.db')
# Cursor erzeugen
cursor = connection.cursor()


def drop_db():
    cursor.execute(""" DROP TABLE IF EXISTS person; """)


def create_tables():
    # Cursor kann beliebige SQL Anweisungen ausführen
    cursor.execute(
        """
        CREATE TABLE person (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vorname TEXT,
            passwort TEXT,
            email TEXT
            )
        """)


def insert_data():
    cursor.execute(
        """
        INSERT INTO person (
            vorname,
            passwort,
            email
            )
        VALUES
            ("Kai", "geheim", "kai@mail.com"),
            ("Tux", "linux", "tux@mail.com"),
            ("Karlos", "1234", "karlos@mail.com")
        """)


drop_db()
create_tables()
insert_data()

# Ánderungen an DB übertragen
connection.commit()
# Verbindung schliessen
connection.close()
