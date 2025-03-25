import json  # Importiert das Modul zum Arbeiten mit JSON-Daten.
import random  # Importiert das Modul für zufällige Auswahl.
import os  # Importiert das Modul für Betriebssystem-Funktionen.

# Funktion zum Laden der Datenbank aus einer JSON-Datei.
def lade_datenbank(datei_pfad=os.path.join(os.path.dirname(__file__), "datenbank.json")):
    with open(datei_pfad, "r", encoding="utf-8") as file:  # Öffnet die Datei im Lese-Modus mit UTF-8-Kodierung.
        return json.load(file)  # Lädt und gibt den Inhalt der JSON-Datei als Python-Datenstruktur zurück.

datenbank = lade_datenbank()  # Lädt die Datenbank und speichert sie in der Variable `datenbank`.

# Funktion, die auf Benutzereingaben reagiert und eine Antwort generiert.
def chatbot_antwort(eingabe):
    eingabe = eingabe.lower()  # Wandelt die Eingabe in Kleinbuchstaben um.
    # Liste von möglichen Begrüßungen.
    begruessungen = ["hallo", "hi", "moin", "guten tag", "was geht", "servus", "hey",
                     "hallochen", "na", "tag", "guten Abend", "moin moin", "guten Morgen"]
    # Überprüft, ob ein Schlüsselwort aus der Datenbank in der Eingabe enthalten ist.
    for schluesselwort in datenbank:
        if schluesselwort in eingabe and schluesselwort != "fallback":  # Ignoriert den "fallback"-Schlüssel.
            antwort = datenbank[schluesselwort]  # Holt die Antwort aus der Datenbank.
            if isinstance(antwort, list):  # Prüft, ob die Antwort eine Liste ist.
                return random.choice(antwort)  # Gibt eine zufällige Antwort aus der Liste zurück.
            return antwort  # Gibt die Antwort direkt zurück, wenn sie kein Liste ist.
    # Überprüft, ob die Eingabe eine Begrüßung enthält.
    for begruessung in begruessungen:
        if begruessung in eingabe:
            return random.choice(datenbank["begrüßung"])  # Gibt eine zufällige Begrüßung aus der Datenbank zurück.
    
    return random.choice(datenbank["fallback"])  # Gibt eine zufällige Fallback-Antwort zurück, wenn nichts passt.

# Hauptprogramm, das den Chatbot in einer Schleife ausführt.
if __name__ == "__main__":
    while True:  # Endlosschleife für den Chatbot.
        frage = input("Frage mich etwas über die Kubakrise: ")  # Fragt den Benutzer nach einer Eingabe.
        if frage.lower() in ["exit", "quit", "ende"]:  # Beendet die Schleife, wenn der Benutzer "exit", "quit" oder "ende" eingibt.
            print("Bis bald!")  # Gibt eine Abschieds-Nachricht aus.
            break  # Bricht die Schleife ab.
        print(chatbot_antwort(frage))  # Gibt die Antwort des Chatbots auf die Eingabe aus.