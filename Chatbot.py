import customtkinter as ctk


# Fonction de réponse du chatbot
def chatbot_response(user_input):
    responses = {
        "bonjour": "Bonjour ! Comment puis-je vous aider ?",
        "comment ça va ?": "Je suis un programme d'un Hacker, donc je vais toujours super bien !",
        "des scripts": "Oui, j'ai des scripts basiques que je peux vous partager dans un cadre éthique et légal",
        "au-revoir": "Au-revoir ! Passez une excellente journée !",
        "comment tu vas ?": "Je suis un programme informatique en constante évolution, donc je vais bien !",
        "connais-tu des scripts": "Oui, j'en connais mais qui sont dans un cadre légal et autorisé",
        "donnes-moi des exemples": "ping 192.168.1.1, tracerout www.google.com et nslookup www.google.com"
    }
    return responses.get(user_input.lower(), "Désolé, je n'ai pas compris. Peux-tu reformuler ou contacter un expert ?")


# Fonction pour  gérer l'envoi des messages
def send_message(event=None):
    user_message = user_input.get()
    if user_message.strip()!= "":
        chat_history.configure(state="normal")
        chat_history.insert("end", f"Vous: {user_message}.\n", "user")
        bot_response = chatbot_response(user_message)
        chat_history.insert("end", f"Bot: {bot_response},\n", "bot")
        chat_history.configure(state="disabled")
        chat_history.see("end")
        user_input.delete(0, "end")
    

# Configurer l'interface graphique 
app = ctk.CTk()
app.geometry("500x600")
app.title("Chatbot ITHACKER")

# En-tête
header = ctk.CTkLabel(app, text="Bienvenue sur le catbot de ITHACKER", font=("Arial", 18, "bold"))
header.pack(pady=10)

# Zone d'affichage des messages 
chat_history = ctk.CTkTextbox(app, height=400, state="disabled")
chat_history.tag_config("user", foreground="white")
chat_history.tag_config("bot", foreground="green")
chat_history.pack(pady = 10, padx = 10, fill="both", expand = True)


# Champ de saisie utilisateur
user_input_frame = ctk.CTkFrame(app)
user_input_frame.pack(pady=10, padx=10, fill="x")

user_input = ctk.CTkEntry(user_input_frame, placeholder_text="Entrz votre message ici...", width=350)
user_input.pack(side="left", padx=5)

send_button = ctk.CTkButton(user_input_frame, text="Envoyer", command=send_message)
send_button.pack(side="left")



#Associer la touche "Entrée" au champ de saisie pour envoyer le message
app.bind("<Return>", send_message)



app.mainloop()