# JARVIS - Virtual Voice Assistant with Face Recognition 
JARVIS is an advanced virtual assistant built using Python that combines face recognition, speech recognition, text-to-speech, and automation to act as a personal assistant. It can recognize authorized users via webcam, understand voice commands, speak back to the user, and perform actions like telling jokes, fetching weather updates, opening websites, launching apps, and even typing for the user.

✨ Features
✅ Face Recognition Login
🎤 Voice Commands
🗣️ Text-to-Speech Responses
🌐 Weather Updates (via OpenWeather API)
😂 Joke Telling (via Joke API)
📺 Open YouTube or Other Sites
⏰ Tell Current Time
🔠 Type Custom Text Automaticall
💻 Launch Desktop Applications
🔒 Secure Exit or System Shutdown

🛠️ Prerequisites:
Python 3.8 or higher
pip install face_recognition opencv-python speechrecognition pyttsx3 requests pyautogui pyaudio

📁 Folder Structure
project/
│
├── jarvis.py              # Main assistant file
└── static/
    └── known_faces/       # Folder with images of known users
                            # Example: john.jpg, alice.jpg


🧪 Example Commands to Try
"What’s the weather"
"Tell me a joke"
"Open YouTube"
"What time is it"
"Type Hello World"
"Call<name>"
"Shutdown"
"Exit"

🧠 Customization
Add known faces to static/known_faces/ as .jpg or .png.
Replace your_openweather_api_key with your actual OpenWeather API key.
Add more elif blocks in start_voice_assistant() to support more commands.

