import webbrowser
from core.voice import speak
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()


# Task: Open Websites
def open_website(website):
    if website == "google":
        webbrowser.open("https://www.google.com")
    elif website == "youtube":
        webbrowser.open("https://www.youtube.com")
    elif website == "linkedin":
        webbrowser.open("https://www.linkedin.com/feed/")
    elif website == "github":
        webbrowser.open(os.getenv("GITHUB"))
    elif website == "chatgpt":
        webbrowser.open("https://chatgpt.com/")
    elif website == "flex":
        open_flex_and_autofill()
    elif website == 'classroom':
        webbrowser.open("https://classroom.google.com/u/1/?emr=0&pli=1")
    elif website == "university gmail":
        webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
    elif website == "personal gmail":
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    else:
        speak("Website not found.")

# Task: Search on Websites
def search_on_website(query, website):
    if website == "google":
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f'Searching Google for {query}...')
    elif website == "youtube":
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        speak(f'Searching YouTube for {query}...')


# Task: Open FLEX and Autofill Login Details
def open_flex_and_autofill():
    speak("Opening FLEX...")
    driver_path = os.getenv("CHROME_DRIVER")
    roll_number = os.getenv("ROLL_NUMBER")
    password = os.getenv("FLEX_PASSWORD")

    if not roll_number or not password:
        speak("Roll number or password is missing. Please check the environment file.")
        return
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://flexstudent.nu.edu.pk/Login")
    time.sleep(2)
    try:
        roll_number_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "m_inputmask_4"))
        )
        password_field = driver.find_element(By.ID, "pass")

        roll_number_field.send_keys(roll_number)
        password_field.send_keys(password)

        # login_button = driver.find_element(By.ID, "m_login_signin_submit")
        # login_button.click()
        time.sleep(5)
        speak("Autofilled the login details, but did not log in.")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")
