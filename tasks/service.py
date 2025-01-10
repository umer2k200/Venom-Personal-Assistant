import os
from core.voice import speak
from dotenv import load_dotenv
load_dotenv()

# Task: Open Services
def open_services(service):
    if service == "vscode":
        vscode_path = os.getenv("VSCODE")
        if os.path.exists(vscode_path):
            os.startfile(vscode_path)
            speak("Opening VS Code...")
        else: 
            speak("VS Code not found on the system!")
    elif service =="chrome":
        chrome_path = os.getenv("CHROME")
        if os.path.exists(chrome_path):
            os.startfile(chrome_path)
            speak("Opening Google Chrome...")
        else:
            speak("Google Chrome not found on the system!")

# Task: Close Services
def close_services(service):
    if service == "chrome":
        chrome_path = os.getenv("CHROME")
        if os.path.exists(chrome_path):
            os.system(f"taskkill /im chrome.exe /f")
            speak("Closing Google Chrome...")
        else:
            speak("Google Chrome not found on the system!")
    elif service == "vscode":
        vscode_path = os.getenv("VSCODE")
        if os.path.exists(vscode_path):
            os.system(f"taskkill /im Code.exe /f")
            speak("Closing VS Code...")
        else:
            speak("VS Code not found on the system!")
