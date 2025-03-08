from flask import Flask, render_template, request
from chatbot import chatbot_antwort 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    antwort = ""
    if request.method == "POST":
        frage = request.form.get("frage")
        if frage:
            antwort = chatbot_antwort(frage)
    return render_template("index.html", antwort=antwort)

if __name__ == "__main__":
    app.run(debug=True)
