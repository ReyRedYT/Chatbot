import json
import random
import os
from google import genai

def lade_datenbank(datei_pfad=os.path.join(os.path.dirname(__file__), "datenbank.json")):
    with open(datei_pfad, "r", encoding="utf-8") as file:
        return json.load(file)
    
datenbank = lade_datenbank()

def frage_gemini(question):
    client = genai.Client(api_key="API_KEY")
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=question
    )
    return response.text

def chatbot_antwort(eingabe):
    eingabe = eingabe.lower()
    begruessungen = ["hallo", "hi", "moin", "guten tag", "was geht", "servus", "hey",
                     "hallochen", "na", "tag", "guten Abend", "moin moin", "guten Morgen"]
    # Zuerst: Suche in der lokalen Datenbank
    for schluesselwort in datenbank:
        if schluesselwort in eingabe and schluesselwort != "fallback":
            antwort = datenbank[schluesselwort]
            if isinstance(antwort, list):
                return random.choice(antwort)
            return antwort
    # Separat: Begrüßungen behandeln
    for begruessung in begruessungen:
        if begruessung in eingabe:
            return random.choice(datenbank["begrüßung"])
    
    # Fallback: Bei unbekannten Fragen wird nun Gemini abgefragt
    return frage_gemini(eingabe)

if __name__ == "__main__":
    while True:
        frage = input("Frage mich etwas über den kalten Krieg oder andere Themen: ")
        if frage.lower() in ["exit", "quit", "ende"]:
            print("Bis bald!")
            break
        print(chatbot_antwort(frage))
