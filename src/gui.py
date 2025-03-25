from flask import Flask, render_template, request  # Importiert Flask und Funktionen für Templates und HTTP-Anfragen
from chatbot import chatbot_antwort  # Importiert die Funktion, die die Antwort des Chatbots liefert

app = Flask(__name__)  # Erstellt eine Flask-Anwendung
verlauf = []  # Initialisiert eine Liste, um den Verlauf von Fragen und Antworten zu speichern

@app.route("/", methods=["GET", "POST"])  # Definiert die Route für die Startseite und erlaubt GET- und POST-Anfragen
def index():  # Definiert die Funktion, die ausgeführt wird, wenn die Startseite aufgerufen wird
    antwort = ""  # Initialisiert die Antwort als leeren String
    if request.method == "POST":  # Prüft, ob eine POST-Anfrage gesendet wurde
        frage = request.form.get("frage")  # Holt die Frage aus dem Formular
        if frage:  # Prüft, ob eine Frage übermittelt wurde
            antwort = chatbot_antwort(frage)  # Ruft die Antwort des Chatbots ab
            verlauf.append({"frage": frage, "antwort": antwort})  # Speichert die Frage und Antwort im Verlauf
    return render_template("index.html", antwort=antwort, verlauf=verlauf)  # Rendert die HTML-Seite mit Antwort und Verlauf

if __name__ == "__main__":  # Prüft, ob das Skript direkt ausgeführt wird
    app.run(debug=True)  # Startet den Flask-Server im Debug-Modus