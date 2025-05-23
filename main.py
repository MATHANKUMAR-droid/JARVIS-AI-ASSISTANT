import face_recognition
import cv2
import os
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import time
import sys
import pyautogui
import subprocess

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def get_weather(city="Delhi"):
    API_KEY = "your_openweather_api_key"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url).json()
        temp = res['main']['temp']
        desc = res['weather'][0]['description']
        return f"It's currently {temp}°C with {desc} in {city}."
    except:
        return "I couldn't fetch the weather right now."

def tell_joke():
    try:
        res = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        return f"{res['setup']} ... {res['punchline']}"
    except:
        return "I couldn't find a joke at the moment."

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
    except Exception:
        speak("Sorry, I didn't catch that.")
        return None
    return query.lower()

def open_application(app_name):
    try:
        if sys.platform.startswith('win'):
            app_paths = {
                "notepad": "notepad.exe",
                "calculator": "calc.exe",
                "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
            }
            if app_name in app_paths:
                os.startfile(app_paths[app_name])
            else:
                speak(f"I don't know how to open {app_name}. Please add its path.")
                return
        elif sys.platform.startswith('linux') or sys.platform == "darwin":
            subprocess.Popen([app_name])
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Unable to open {app_name}. Error: {str(e)}")

def type_text(text):
    speak("Typing now...")
    time.sleep(2)
    pyautogui.write(text, interval=0.05)

def simulate_call(name):
    speak(f"Calling {name}... just kidding, I'm not connected to a phone network yet!")

def start_voice_assistant(user):
    speak(f"Hello {user}, how can I assist you today?")
    while True:
        command = get_command()
        if not command:
            continue

        if "weather" in command:
            weather = get_weather()
            speak(weather)

        elif "joke" in command:
            joke = tell_joke()
            speak(joke)

        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}")

        elif "shutdown" in command:
            speak("Shutting down system.")
            os.system("shutdown /s /t 1")

        elif "open" in command:
            app = command.replace("open ", "").strip()
            open_application(app)

        elif "type" in command:
            speak("What should I type?")
            to_type = get_command()
            if to_type:
                type_text(to_type)

        elif "call" in command:
            name = command.replace("call ", "").strip()
            simulate_call(name)

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

def recognize_face():
    known_faces = {}
    path = "static/known_faces"

    if not os.path.exists(path):
        os.makedirs(path)
        speak("No known faces found. Please add images to 'static/known_faces'.")
        return None

    for file in os.listdir(path):
        img = face_recognition.load_image_file(f"{path}/{file}")
        encodings = face_recognition.face_encodings(img)
        if encodings:
            known_faces[file.split(".")[0]] = encodings[0]

    if not known_faces:
        speak("No encodings found. Ensure images contain clear faces.")
        return None

    video = cv2.VideoCapture(0)
    recognized_name = None

    while True:
        ret, frame = video.read()
        rgb_frame = frame[:, :, ::-1]
        faces = face_recognition.face_locations(rgb_frame)
        encodings = face_recognition.face_encodings(rgb_frame, faces)

        for face_encoding in encodings:
            for name, known_encoding in known_faces.items():
                match = face_recognition.compare_faces([known_encoding], face_encoding)[0]
                if match:
                    recognized_name = name
                    video.release()
                    cv2.destroyAllWindows()
                    return recognized_name

        cv2.imshow("Recognizing Face... Press 'q' to cancel.", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    return None

def main():
    user = recognize_face()
    if user:
        print(f"Welcome, {user}!")
        start_voice_assistant(user)
    else:
        print("Face not recognized. Access denied.")
        speak("Face not recognized. Access denied.")

if __name__ == "__main__":
    main()

