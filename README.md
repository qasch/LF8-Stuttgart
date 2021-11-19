
# Notizen

## Dieses Repository benutzen

Um die App so wie sie hier vorliegt auf dem eigenen Rechner starten zu können, sind folgende Schritte nötig:

- Repository clonen (mit Git) ODER
- Zip Datei herunterladen und entpacken
- Im Ordner **flask-app** ein VirtualEnv erzeugen (über die IDE oder die Kommandozeile)
- das VirtualEnv aktivieren
- benötigte Python Module und Abhängigkeiten installieren mit **pip -r requirements.txt**
- App starten über die IDE oder über die Kommandozeile mit **python app.py**

Die Datei **requirements.txt** enthält eine Liste der benötigten Module, die für den
Betrieb der APP nötig sind. Diese Datei kann mit dem Kommando **pip freeze > requirements.txt** erzeugt bzw. aktualisiert werden. Weitere Informationen hierüber findet ihr in der Dokumentation von *Flask* oder von **pip**.

## Ausführung von Skripten ist nicht erlaubt

### Powershell als Administrator starten und Policies prüfen:

  `Get-ExecutionPolicy`

### Ausführungsrechte setzen:

  `Set-ExecutionPolicy RemoteSigned`

## Virtual Environment aktivieren

Im Pycharm unter 'Terminal' folgendes eingeben:

  `venv\Scripts\activate`

## Flask installieren

  `pip install Flask`
