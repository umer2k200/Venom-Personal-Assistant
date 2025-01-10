import os
from core.voice import speak, listen
import requests
from bs4 import BeautifulSoup
import datetime
import time
import pyautogui
from dotenv import load_dotenv
load_dotenv()


# Task: Tell Current Time
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")

# Task: Tell Weather
def tell_weather():
    search = "temperature in Islamabad"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    temp = soup.find("div", class_ = "BNeawe").text
    speak(f"Current {search} is {temp}")


# Task: Open Resume
def open_resume():
    resume_path = os.getenv("RESUME")
    if os.path.exists(resume_path):
        os.startfile(resume_path)
        speak("Opening resume...")
    else:
        speak("Resume not found on the system!")

# Task: Take Screenshot
def take_screenshot():
    screenshot_path = os.getenv("SCREENSHOT")
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    speak("what should I name the screenshot?")
    screenshot_name = listen(True)
    if screenshot_name:
        screenshot_name = f"{screenshot_name}.png"
    else:
        screenshot_name = f"screenshot_{current_time}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{screenshot_path}/{screenshot_name}")
    speak("Screenshot taken successfully.")
