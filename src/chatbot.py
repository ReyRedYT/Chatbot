import json
import random
import os

def lade_datenbank(datei_pfad=os.path.join(os.path.dirname(__file__), "datenbank.json")):
    with open(datei_pfad, "r", encoding="utf-8") as file:
        return json.load(file)
    
datenbank = lade_datenbank()

def chatbot_antwort(eingabe):
    eingabe = eingabe.lower()
    for schluesselwort in datenbank:
        if schluesselwort in eingabe and schluesselwort != "fallback":
            antwort = datenbank[schluesselwort]
            if isinstance(antwort, list):
                return random.choice(antwort)
            return antwort
    
    return random.choice(datenbank["fallback"])

if __name__ == "__main__":
    while True:
        frage = input("Frage mich etwas über deutsche Politik und Geschichte oder stelle eine allgemeine Frage: ")
        if frage.lower() in ["exit", "quit", "ende"]:
            print("Bis bald!")
            break
        print(chatbot_antwort(frage))