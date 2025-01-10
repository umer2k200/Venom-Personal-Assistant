from core.voice import speak
import os
import speech_recognition as sr
from dotenv import load_dotenv
load_dotenv()

def authentication():
    speak("Authentication required! please say the password.")
    for i in range(3):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that.")
                return None
            except sr.RequestError:
                speak("Network error. Please check your internet connection.")
                return None
            except sr.WaitTimeoutError:
                speak("You were silent for too long.")
                return None
        
        if os.getenv("CODE") in command:
            speak("Authentication successful!")
            return True
        elif os.getenv("CODE2") in command:
            speak("So that we can learn to pick ourselves up")
            return True
        elif os.getenv("CODE3") in command:
            speak("Men are brave!")
            return True
        else:
            if i < 2:
                speak(f"Wrong Password! Try again.")
    return False
