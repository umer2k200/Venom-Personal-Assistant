from tasks.authentication import authentication
from core.voice import speak
from core.launcher import venom_launcher

def main():
    auth = authentication()
    if auth:
        venom_launcher()
    else:
        speak("Authentication failed after three attempts.")

if __name__ == "__main__":
    main()
