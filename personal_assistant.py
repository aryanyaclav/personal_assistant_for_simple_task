import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui
import sys

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

# creating chrome path to open query in chrome rather then IE
c = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# giving chrome path to WB
w = webbrowser.get(c)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("hello ,tell me to do something")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='eng-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing task based on query

        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak(results)

        elif 'open youtube' in query:
            w.open('youtube.com')

        elif 'open google' in query:
            w.open('google.com')

        elif 'tinder' in query:
            w.open('tinder.com')
            speak("say yes if you like ,or say no, if you do not like")
            s=True
            while s :
                swipe= takeCommand().lower()
                if 'yes' in swipe:
                    pyautogui.click(x=921,y=593)
                elif 'no' in swipe:
                    pyautogui.click(x=780,y=592)
                elif 'thank you' in swipe:
                    speak("enough for today")
                    s=False

        elif 'about' in query:
            speak("my name is bulbul ,i am created by using python")



        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'sleep' in query:
            speak('i am taking nap , call me if you need any help')
            sys.exit()






