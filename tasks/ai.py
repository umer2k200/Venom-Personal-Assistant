import openai
import os
from core.voice import speak,listen
from dotenv import load_dotenv
load_dotenv()

# Task: AI Response (e.g., ChatGPT)
def get_ai_response(command):
    speak("What would you like to ask?")
    query = listen()
    if query:
        openai.api_key = os.getenv("OPEN_AI_API_KEY")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}]
            )
            answer = response['choices'][0]['message']['content']
            speak(answer)
        except openai.error.RateLimitError:
            speak("It seems I've reached my API request limit. Please try again later.")
        except openai.error.InvalidRequestError as e:
            speak(f"Invalid request: {str(e)}")
        except openai.error.AuthenticationError:
            speak("Authentication failed. Please check your API key.")
        except Exception as e:
            speak(f"An unexpected error occurred: {str(e)}")
