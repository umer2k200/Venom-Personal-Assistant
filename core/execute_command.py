from tasks.ai import get_ai_response
from tasks.service import open_services, close_services
from tasks.system_initiate import Initiate_system
from tasks.system import shutdown, restart, sleep_pc, change_volume, change_brightness, open_folder
from tasks.utility import tell_time, tell_weather, open_resume, take_screenshot
from tasks.web import open_website, search_on_website
from core.voice import speak

# Execute Commands Dynamically
def execute_command(command):
    if "shutdown the system" in command or "turn off the system" in command:
        speak("Shutting down the system...")
        shutdown()
    elif "restart the system" in command:
        speak("Restart Initiated...")
        restart()
    elif "sleep pc" in command or "sleep system" in command:
        speak("Putting the system to sleep...")
        sleep_pc()
    elif "volume" in command:
        change_volume(command)
    elif "brightness" in command:
        change_brightness(command)
    elif "open" in command:
        if "youtube" in command:
            open_website("youtube")
            speak("Opening YouTube...")
        elif "google" in command:
            open_website("google")
            speak("Opening Google...")
        elif "linkedin" in command:
            open_website("linkedin")
            speak("Opening LinkedIn...")
        elif "github" in command:
            open_website("github")
            speak("Opening GitHub...")
        elif "chat gpt" in command:
            open_website("chatgpt")
            speak("Opening ChatGPT...")
        elif "flex" in command:
            open_website("flex")
        elif "classroom" in command:
            open_website("classroom")
            speak("Opening Classroom...")
        elif "university gmail" in command:
            open_website("university gmail")
            speak("Opening univeristy gmail inbox...")
        elif "personal gmail" in command:
            open_website("personal gmail")
            speak("Opening personal gmail inbox...")
        elif "vs code" in command:
            open_services("vscode")
        elif "chrome" in command:
            open_services("chrome")
        elif "folder" in command:
            folder_name = command.replace("open", "").replace("folder", "").strip()
            open_folder(folder_name)
        elif "resume" in command:
            open_resume()

    elif "close" in command:
        if "chrome" in command:
            close_services("chrome")
        elif "vs code" in command:
            close_services("vscode")

    elif "search" in command:
        if "google" in command:
            search_query = command.replace("search", "").replace("on google", "").strip()
            search_on_website(search_query, "google")
        elif "youtube" in command:
            search_query = command.replace("search", "").replace("on youtube", "").strip()
            search_on_website(search_query, "youtube")

    elif "time" in command:
        tell_time()
    elif "weather" in command or "temperature" in command:
        tell_weather()
    elif "prepare the system" in command or "prepare everything" in command or "begin my routine" in command or "activate my setup" in command:
        Initiate_system()
    elif "screenshot" in command:
        take_screenshot()
    elif "ai response" in command:
        get_ai_response(command)
    
    else:
        speak("Sorry, I can't perform this task yet.")

