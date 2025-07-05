# 🧠 AI Chat GUI with Text-to-Speech (TTS)

Welcome to my **AI Chat Interface** project — a part of my journey in learning Python through real-world applications.  
This project demonstrates how to build a **functional AI assistant with chat memory, TTS, and user authentication** using Python and modern tools.

---

## 📚 About the Project

This project is built using **Python** and serves as a practical learning exercise in:
- GUI design with `Tkinter`
- AI integration using `Ollama` and `Gemma 3B` (here)
- Speech synthesis using **ElevenLabs**
- MongoDB-based user authentication system
- Modular coding and multi-file architecture

It’s an effort to blend AI interaction with a user-friendly and accessible desktop app.

---

## 🔧 Libraries / Modules Used

| Library         | Purpose                                   |
|----------------|-------------------------------------------|
| `tkinter`       | GUI (Graphical User Interface)           |
| `pymongo`       | MongoDB integration for login & settings |
| `dotenv`        | Load environment variables securely       |
| `os`            | Work with environment/system paths        |
| `ollama`        | Connect to locally running LLMs (Gemma)   |
| `threading`     | Run AI stream without freezing the UI     |
| `elevenlabs`    | TTS voice synthesis from AI response      |

---

## ✨ Features

- ✅ **Login System** with MongoDB
- ✅ **Dashboard** with a chat display and input area
- ✅ **Streaming AI Responses** from Ollama (here `gemma3:1b`)
- ✅ **Text-to-Speech Button** powered by ElevenLabs
- ✅ **Settings Panel** to:
  - Change username
  - Change login credentials (with user authentication before changing the credentials)
- ✅ **Logout Button** that redirects back to the login screen
- ✅ **Clean and modern interface** with theme color

---

## 📁 Project Directory Structure

```
AI Chat GUI/
├── main.py # Login window
├── board.py # Dashboard and chat logic
├── settings.py # Settings window (change name & credentials)
├── logo_1.png # Logo used in settings UI (you may upload your logo)
├── .env # Contains API keys of ElevenLabs and MongoDB URI
├── .gitignore # Ignores .env and pycache
└── README.md # The documentation file

```

---

## 🏁 Conclusion

This project is a reflection of my growth in Python — from basic syntax to building an integrated AI application. I built this project to:

- Practice real-world coding patterns
- Learn how to connect multiple services (LLMs, TTS, DBs)
- Create something I can proudly showcase in my portfolio

> Feel free to fork, learn from, and improve this project. Enjoy coding!

---

## Important Links
- (https://elevenlabs.io/docs/quickstart)
- (https://github.com/ollama/ollama-python)
- (https://ollama.com/)
- (https://cloud.mongodb.com/)

---
