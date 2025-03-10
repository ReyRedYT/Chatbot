from google import genai


def chatbot():
    client = genai.Client(api_key="API_KEY")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents = question)
    print(response.text)

if __name__ == "__main__":
    while True:
        question = input("Was möchtest du wissen?: ")
        if question.lower() in ["exit", "quit", "ende"]:
            print("Bis bald!")
            break
        print(chatbot())