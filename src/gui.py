from flask import Flask, render_template, request
from chatbot import chatbot_antwort 

app = Flask(__name__)
verlauf = []

@app.route("/", methods=["GET", "POST"])
def index():
    antwort = ""
    if request.method == "POST":
        frage = request.form.get("frage")
        if frage:
            antwort = chatbot_antwort(frage)
            verlauf.append({"frage": frage, "antwort": antwort})
    return render_template("index.html", antwort=antwort, verlauf=verlauf)

if __name__ == "__main__":
    app.run(debug=True)