from core.voice import speak, listen
from core.execute_command import execute_command
import time
import random

# Greet User at start
def greet():
    current_hour = time.localtime().tm_hour
    print(f"Current hour: {current_hour}")
    if current_hour < 12:
        speak("Good morning! it's your Venom. How can I assist you?")
    elif current_hour < 16:
        speak("Good afternoon! it's your Venom. How can I assist you?")
    elif current_hour < 20:
        speak("Good evening! it's your Venom. How can I assist you?")
    else:
        speak("Good night! it's your Venom. How can I assist you?")

def venom_launcher():
    print("Venom Launcher starting...")
    greet()
    while True:
        command = listen()
        #print(f"Command received: {command}")
        if command:
            if any(hello in command for hello in ["hello","hi","hey","hey there","hi there"]):
                speak(random.choice(["Hello! How can I assist you?", "Hi! How can I help you?", "Hey! What can I do for you?", "Hey there! How can I assist you?", "Hi there! How can I help you?"]))
            elif "exit" in command or "quit" in command or "stop" in command: 
                speak("Turning off, sir.")
                break
            elif "bye" in command or "bye venom" in command:
                speak("Bye! Venom is signing off.")
                break
            elif "goodbye" in command:
                speak("Goodbye! Have a great day.")
                break
            elif "goodnight" in command:
                speak("Goodnight! Sweet dreams.")
                break
            else:
                execute_command(command)
