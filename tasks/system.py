import os
import ctypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import screen_brightness_control as sbc
from core.voice import speak
from dotenv import load_dotenv
load_dotenv()

# Task: Shutdown, Restart, Sleep PC
def shutdown():
    os.system("shutdown /s /t 1")

def restart():
    os.system("shutdown /r /t 1")

def sleep_pc():
    ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)

# Task: Volume Control
def set_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)

    volume.SetMasterVolumeLevelScalar(volume_level/100.0, None)
    speak(f"Volume set to {volume_level} percent.")
def change_volume(command):
    if "increase volume" in command:
        set_volume(70)
    elif "decrease volume" in command:
        set_volume(30)
    elif "mute volume" in command:
        set_volume(0)
    elif "set volume to" in command:
        try:
            level = int(command.split("set volume to")[1].strip())
            set_volume(level)
        except ValueError:
            speak("Please specify a valid volume level.")

# Task: Brightness Control
def set_brightness(level):
    try:
        sbc.set_brightness(level)
        speak(f"Brightness set to {level} percent.")
    except Exception as e:
        speak(f"An error occurred while setting brightness: {str(e)}")
def change_brightness(command):
    if "increase brightness" in command:
        current_brightness = sbc.get_brightness()[0]
        set_brightness(min(current_brightness + 20, 100))
    elif "decrease brightness" in command:
        current_brightness = sbc.get_brightness()[0]
        set_brightness(max(current_brightness - 20, 0))
    elif "set brightness to" in command:
        try:
            level = int(command.split("set brightness to")[1].strip())
            set_brightness(level)
        except ValueError:
            speak("Please specify a valid brightness level.")

# Task: Open folders
def open_folder(folder_name):
    folders = {
        "downloads" : os.getenv("DOWNLOADS_FOLDER"),
        "office work" : os.getenv("OFFICE_WORK_FOLDER"),
        "projects" : os.getenv("PROJECTS_FOLDER"),
        "venom" : os.getenv("VENOM_FOLDER"),
        "university" : os.getenv("UNIVERSITY_FOLDER"),
    }
    if folder_name in folders:
        path = folders[folder_name]
        os.startfile(path)
        speak(f"Opening {folder_name} folder...")
    else:
        speak("Folder not found.")
