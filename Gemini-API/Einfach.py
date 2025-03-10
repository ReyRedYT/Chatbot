from google import genai

def chatbot():
    client = genai.Client(api_key="API_KEY")

    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents = frage
    )
    print("")
    print("Nutzer: " + frage)
    return response.text

if __name__ == "__main__":
    while True:
        frage = input("Was möchtest du wissen? ")
        if frage.lower() in ["exit", "quit", "ende"]:
            print("Bis bald!")
            break
        print("Gemini: " + chatbot())