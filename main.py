import pyttsx3
import speech_recognition as sr
import keyboard
import subprocess as sp
import os
import wolframalpha

from decouple import config
from conv import random_text
from random import choice
from online import search_on_wikipedia, search_on_google,youtube,get_news

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

USER=config('USER')
HOST=config('BOT')

def speak(text):
    engine.say(text)
    engine.runAndWait()

listening = False


def start_listening():
    global listening
    listening = True
    print("started listening ")


def pause_listening():
    global listening
    listening = False
    print("stopped listening")


keyboard.add_hotkey('s', start_listening)
keyboard.add_hotkey('p', pause_listening)


def greet_me():
    speak(f"I am {HOST},How may I assist you? {USER}")

def take_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak(choice(random_text))
        else:
            speak("Have a good day sir!")
            exit()

    except Exception:
        speak("Sorry I couldn't understand. Can you please repeat that?")
        queri = 'None'
    return queri


if __name__ == '__main__':   
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you")
                     
            elif "open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.windows.camera:', shell=True)
            
            elif "open notepad" in query:
                speak("Opening Notepad for you sir")
                notepad_path = "C:\\Users\\radha\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe"
                os.startfile(notepad_path)

            elif "open youtube" in query:
                speak("What do you want to play on youtube sir?")
                video = take_command().lower()
                youtube(video)

            elif "open google" in query:
                speak(f"What do you want to search on google {USER}")
                query = take_command().lower()
                search_on_google(query)

            elif "wikipedia" in query:
                speak("what do you want to search on wikipedia sir?")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"According to wikipedia,{results}")
                speak("I am printing in on terminal")
                print(results)  
                search_on_wikipedia(search)

            elif "give me news" in query:
                speak(f"I am reading out the latest headline of today,sir")
                speak(get_news())
                speak("I am printing it on screen sir")
                print(*get_news(), sep='\n')
            
            elif "calculate" in query:
                app_id = "JJ6JKK-UK2JU5Y5L6"
                client = wolframalpha.Client(app_id)
                ind = query.lower().split().index("calculate")
                text = query.split()[ind + 1:]
                result = client.query(" ".join(text))
                try:
                    ans = next(result.results).text
                    speak("The answer is " + ans)
                    print("The answer is " + ans)
                except StopIteration:
                    speak("I couldn't find that . Please try again")

           
