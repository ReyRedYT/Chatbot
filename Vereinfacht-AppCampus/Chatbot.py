import requests

def classify(text):
    
    key = "02c8d050-fc21-11ef-a617-2b8edcbb5fd885060609-f645-4679-a5f4-4b972f0a40d7"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():

    eingabe = input("Frage: ")
    klassifikation = classify(eingabe)
    label = klassifikation["class_name"]

    if label == "Allgemein":
        print("Der Kalte Krieg war ein ideologischer und geopolitischer Konflikt zwischen den beiden Supermächten USA und Sowjetunion, der von 1947 bis 1991 andauerte.")

print("Willkommen beim Chatbot")
while True:
    answer_question()