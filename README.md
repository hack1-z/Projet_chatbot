````markdown
# 🤖 Chatbot ITHACKER  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)  
![Tkinter](https://img.shields.io/badge/CustomTkinter-UI-green?logo=codeigniter)  
![Status](https://img.shields.io/badge/Status-Dev-orange)  

Un **chatbot personnel** en Python avec une interface graphique moderne grâce à **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)**.  
💡 Objectif : apprendre à créer des applications GUI, manipuler des événements et gérer des réponses basiques sous forme de dictionnaire.  

---

## ✨ Fonctionnalités
- Interface graphique moderne et responsive (CustomTkinter).  
- Conversation fluide avec historique affiché.  
- Envoi des messages via **Entrée** ou bouton **Envoyer**.  
- Réponses prédéfinies extensibles (dictionnaire).  
- Messages utilisateur en blanc, réponses du bot en vert.  

---

## 🚀 Démo
*(Ajoute ici une capture d’écran ou un GIF de ton app)*  

```bash
python Chatbot.py
````

Exemple d’interaction :

```
Vous: bonjour
Bot: Bonjour ! Comment puis-je vous aider ?
```

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/<ton-utilisateur>/<ton-repo>.git
cd <ton-repo>
```

### 2. Créer un environnement virtuel (optionnel)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

> Si le fichier `requirements.txt` n’existe pas encore, installe simplement :

```bash
pip install customtkinter
```

---

## 🛠️ Utilisation

Lance l’application :

```bash
python main.py
```

Tapez votre message → appuyez sur **Entrée** ou cliquez sur **Envoyer**.

Exemples de commandes comprises par défaut :

* `bonjour`
* `comment ça va ?`
* `des scripts`
* `donnes-moi des exemples`
* `au-revoir`

---

## 📂 Structure du projet

```
├── main.py          # Script principal avec l'UI et la logique
├── README.md        # Ce fichier
└── requirements.txt # Dépendances (optionnel)
```

---

## ⚙️ Personnalisation

* **Ajouter vos propres réponses** :
  Dans `chatbot_response`, modifiez le dictionnaire :

  ```python
  responses = {
      "salut": "Salut 👋",
      "ton nom": "Je suis ITHACKER Bot !"
  }
  ```
* **Changer le thème** :
  CustomTkinter permet de passer en mode `dark` ou `light`.

---

## ⚖️ Éthique & légalité

🔒 Ce projet est **strictement éducatif**.
❌ Aucun script illégal ou dangereux n’est fourni.
✅ Utilisez-le pour apprendre à coder un chatbot, pas pour pirater.

> L’auteur décline toute responsabilité en cas d’utilisation inappropriée. Respectez la loi et testez uniquement dans un cadre légal.

---

## 🤝 Contributions

Les contributions sont les bienvenues !

* Ouvrez une **issue** pour proposer une idée
* Créez une **pull request** pour une amélioration

---

## 📜 Licence

Distribué sous licence **MIT**. Vous êtes libre de l’utiliser, le modifier et le partager tant que vous respectez les termes de la licence.

---

💡 *Made with passion by [Ton Nom / GitHub](https://github.com/hack1-z)* 🚀

```

