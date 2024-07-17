import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary 
import requests


recognizer=sr.Recognizer()
newsapi="5f90e0c2e10d4de0b8d285cac7a32ea5"
engine = pyttsx3.init()
def speak(text):
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. o for male
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
      webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")  
    elif c.lower().startswith("play"):
       song=c.lower().split(" ")[1]
       link=musicLibrary.music[song]
       webbrowser.open(link)

    elif "news" in c.lower():
    
         r=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={newsapi}")
      
   
         if r.status_code == 200:
          data = r.json()
          articles = data.get('articles',[])
          for article in articles:
            speak(article["title"])
         else:
          print(f"Error fetching articles: Status Code {r.status_code}")

if __name__=="__main__":
    speak("Initializing Jarvis...")
 
    #Listen for the wake word 'Jarvis'

    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()
        

        # recognize speech using google
        try:
         with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2)
            word=r.recognize_google(audio)

         if(word.lower()=="hey jarvis"):
            speak("Yes Radha , what it is ?")
         with sr.Microphone() as source:
            print("Jarvis Active")
            audio = r.listen(source, timeout=2)
            command=r.recognize_google(audio)

            processCommand(command)

        except Exception as e:
         print("Error; {0}".format(e))
      
    