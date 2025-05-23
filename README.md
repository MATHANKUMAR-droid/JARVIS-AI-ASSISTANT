# 🧠 JARVIS - Virtual Voice Assistant with Face Recognition

JARVIS is an advanced virtual assistant built using Python that combines face recognition, speech recognition, text-to-speech, and automation to act as a personal assistant. It can recognize authorized users via webcam, understand voice commands, speak back to the user, and perform actions like telling jokes, fetching weather updates, opening websites, launching apps, and even typing for the user.

---

## ✨ Features

- ✅ **Face Recognition Login**  
- 🎙️ **Voice Commands**  
- 🗣️ **Text-to-Speech Responses**  
- 🌐 **Weather Updates** (via OpenWeather API)  
- 😂 **Joke Telling** (via Joke API)  
- 📺 **Open YouTube or Other Sites**  
- 🕒 **Tell Current Time**  
- 🔠 **Type Custom Text Automatically**  
- 💻 **Launch Desktop Applications**  
- 🔒 **Secure Exit or System Shutdown**

---

## ⚙️ Prerequisites

- Python 3.8 or higher

Install the required libraries:

```bash
pip install face_recognition opencv-python speechrecognition pyttsx3 requests pyautogui pyaudio
If you encounter errors installing pyaudio, try:
pip install pipwin
pipwin install pyaudio

---
📁 Folder Structure
project/
│
├── jarvis.py                  # Main assistant file
└── static/
    └── known_faces/           # Folder with images of known users
        ├── john.jpg
        └── alice.jpg

💬 Example Commands to Try
"What's the weather"
"Tell me a joke"
"Open YouTube"
"What time is it"
"Type Hello World"
"Call [Name]"
"Shutdown"
"Exit"

