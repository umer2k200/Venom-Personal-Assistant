from core.voice import speak
from tasks.web import open_website
from tasks.service import open_services
from tasks.system import open_folder

# Task: Initiate System (Customized)
def Initiate_system():
    speak("Initiating system...")
    open_services("chrome")
    open_website("personal gmail")
    open_website("university gmail")
    open_website("chatgpt")
    open_website("youtube")
    open_services("vscode")
    open_folder("projects")
    #open_folder("university")
    #open_folder("venom")
    speak("System initiated successfully.")

