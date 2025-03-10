from google import genai
import tkinter as tk
from tkinter import scrolledtext, ttk

# Bestehende Funktion, die die Gemini-API nutzt.
def chatbot():
    client = genai.Client(api_key="API_KEY")  # Ersetze "API_KEY" mit deinem echten API-Schlüssel
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=question)
    return response.text

# Funktion, die die Gemini-API anruft
def send_message(event=None):
    global question
    question = entry.get().strip()
    if question.lower() in ["exit", "quit", "ende"]:
        chat_log.config(state="normal")
        chat_log.insert(tk.END, "Bis bald!\n")
        chat_log.config(state="disabled")
        root.after(1000, root.destroy)
    elif question:
        chat_log.config(state="normal")
        chat_log.insert(tk.END, "Du: " + question + "\n", "user")
        entry.delete(0, tk.END)
        # Antwort von Gemini holen
        gemini_response = chatbot()
        chat_log.insert(tk.END, "Gemini: " + gemini_response + "\n\n", "gemini")
        chat_log.config(state="disabled")
        chat_log.yview(tk.END)

# GUI mit Tkinter erstellen (Darkmode)
root = tk.Tk()
root.title("ChatApp mit Gemini")
root.geometry("500x500")
root.configure(bg="#2e2e2e")

# ScrolledText-Widget für den Chat-Verlauf
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#3c3f41", fg="#ffffff",
                                     font=("Arial", 12), bd=0, highlightthickness=0)
chat_log.tag_config("user", foreground="#00ff00")
chat_log.tag_config("gemini", foreground="#ffa500")
chat_log.config(state="disabled")
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Eingabefeld für Nachrichten
entry = tk.Entry(root, font=("Arial", 12), bg="#3c3f41", fg="#ffffff", insertbackground="#ffffff", bd=0)
entry.pack(padx=10, pady=(0,10), fill=tk.X)
entry.focus()
entry.bind("<Return>", send_message)  # Enter-Taste absenden

# Sende-Button (optional, da Enter schon reicht)
send_button = tk.Button(root, text="Senden", font=("Arial", 12),
                        bg="#5a5a5a", fg="#ffffff", activebackground="#777777", command=send_message, bd=0)
send_button.pack(padx=10, pady=(0,10))

root.mainloop()
