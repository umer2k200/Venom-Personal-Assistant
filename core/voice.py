import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 and 2 for female and 1 for male
engine.setProperty('rate', 175)

# Initialize Text-to-Speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Recognize Voice Input
def listen(screenshot=False):
    wake_word="venom"
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm listening...")
        recognizer.adjust_for_ambient_noise(source)
        listening_for_command = False
        while True:
            try:
                if not listening_for_command:
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio).lower()
                    if screenshot:
                        return command
                    if command == wake_word:
                        speak("yes?")
                        listening_for_command = True
                elif listening_for_command:
                    try:
                        audio = recognizer.listen(source, timeout=10)
                        command = recognizer.recognize_google(audio).lower()
                        if command:
                            return command
                    except sr.WaitTimeoutError:
                        speak("You went silent. Say the wake word again to reactivate!")
                        listening_for_command = False
            except sr.WaitTimeoutError:
                if not listening_for_command:
                    pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                speak("Network error. Please check your internet connection.")
                return None
