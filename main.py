import pyttsx3
import speech_recognition
import wikipedia
import requests
import os
import subprocess
import plyer
from bs4 import BeautifulSoup
import datetime
import pyautogui
import random
import speedtest
import sys

# Move local imports to top
from GreetMe import greetme
from keyboard import volumeup, volumedown
from Dictapp import closeappweb
from SearchNow import searchGoogle, searchYoutube
from Calculatenumbers import WolfRamAlpha, Calc
from Whatsapp import sendMessage
from Translator import translategl

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    if sys.platform == "win32":
        os.startfile("alarm.py")
    else:
        subprocess.Popen(["python", "alarm.py"])


# Command functions
def handle_hello(query):
    speak("Hello sir, how are you ?")

def handle_fine(query):
    speak("that's great, sir")

def handle_how_are_you(query):
    speak("Perfect, sir")

def handle_thank_you(query):
    speak("you are welcome, sir")

def handle_introduce(query):
    speak("I'm zira, your personal AI assistant, here to help with a wide range of tasks like answering questions, ")

def handle_pause(query):
    pyautogui.press("k")
    speak("video paused")

def handle_play(query):
    pyautogui.press("k")
    speak("video played")

def handle_mute(query):
    pyautogui.press("m")
    speak("video muted")

def handle_volume_up(query):
    speak("Turning volume up,sir")
    volumeup()

def handle_volume_down(query):
    speak("Turning volume down, sir")
    volumedown()

def handle_open(query):
    if "app" in query:
        query = query.replace("open", "").replace("app", "").strip()
    else:
        query = query.replace("open","").replace("jarvis","").strip()
    pyautogui.press("super")
    pyautogui.typewrite(query)
    pyautogui.sleep(2)
    pyautogui.press("enter")

def handle_close(query):
    closeappweb(query)

def handle_screenshot(query):
    im = pyautogui.screenshot()
    im.save("screenshort.jpg")
    speak("Screenshot saved")

def handle_camera(query):
    pyautogui.press("super")
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    speak("SMILE")
    pyautogui.press("space")

def handle_close_camera(query):
    pyautogui.hotkey("ctrl","w")

def handle_google(query):
    searchGoogle(query)

def handle_youtube(query):
    searchYoutube(query)

def handle_wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "").strip()
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except Exception as e:
        speak("I couldn't find anything on Wikipedia for that.")

def handle_internet_speed(query):
    try:
        speak("Checking internet speed, please wait.")
        wifi = speedtest.Speedtest()
        upload_net = wifi.upload()/1048576
        download_net = wifi.download()/1048576
        print("Wifi Upload Speed is", upload_net)
        print("Wifi download speed is ",download_net)
        speak(f"Wifi download speed is {download_net:.2f} Megabytes per second")
        speak(f"Wifi Upload speed is {upload_net:.2f} Megabytes per second")
    except Exception as e:
        speak("Sorry, I am unable to check the internet speed at the moment.")

def handle_calculate(query):
    query = query.replace("calculate","").replace("jarvis","").strip()
    Calc(query)

def handle_whatsapp(query):
    sendMessage()

def handle_translate(query):
    query = query.replace("jarvis","").replace("translate","").strip()
    translategl(query)

def handle_temperature(query):
    search = "temperature in belgaum"
    url = f"https://www.google.com/search?q={search}"
    try:
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        speak(f"current {search} is {temp}")
    except Exception as e:
        speak("Sorry, I am unable to fetch the temperature right now.")

def handle_weather(query):
    search = "weather in belgaum"
    url = f"https://www.google.com/search?q={search}"
    try:
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        speak(f"current {search} is {temp}")
    except Exception as e:
        speak("Sorry, I am unable to fetch the weather right now.")

def handle_set_alarm(query):
    print("input time example:- 10 and 10 and 10")
    speak("Set the time")
    a = input("Please tell the time :- ")
    alarm(a)
    speak("Done,sir")

def handle_time(query):
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"Sir, the time is {strTime}")

def handle_date(query):
    strTime = datetime.datetime.now().strftime("%d:%m")
    speak(f"Sir, today date is {strTime}")

def handle_finally_sleep(query):
    speak("going to sleep, sir,if you have any questions please weak me up, i am ready to help you again, sir")
    exit()

def handle_remember_that(query):
    rememberMessage = query.replace("remember that","").replace("jarvis","").strip()
    speak("You told me to "+rememberMessage)
    with open("Remember.txt","a") as remember:
        remember.write(rememberMessage + "\n")

def handle_what_do_you_remember(query):
    try:
        with open("Remember.txt","r") as remember:
            content = remember.read()
            if content:
                speak("You told me to " + content)
            else:
                speak("I don't remember anything yet.")
    except FileNotFoundError:
        speak("I don't remember anything yet.")


# Mapping logic
COMMANDS = {
    "hello": handle_hello,
    "i am fine": handle_fine,
    "how are you": handle_how_are_you,
    "thank you": handle_thank_you,
    "introduce yourself": handle_introduce,
    "pause": handle_pause,
    "play": handle_play,
    "mute": handle_mute,
    "volume up": handle_volume_up,
    "volume down": handle_volume_down,
    "open": handle_open,
    "close camera": handle_close_camera,
    "close": handle_close,
    "screenshot": handle_screenshot,
    "take my photo": handle_camera,
    "google": handle_google,
    "youtube": handle_youtube,
    "wikipedia": handle_wikipedia,
    "internet speed": handle_internet_speed,
    "calculate": handle_calculate,
    "whatsapp": handle_whatsapp,
    "translate": handle_translate,
    "temperature": handle_temperature,
    "weather": handle_weather,
    "set an alarm": handle_set_alarm,
    "the time": handle_time,
    "date": handle_date,
    "finally sleep": handle_finally_sleep,
    "remember that": handle_remember_that,
    "what do you remember": handle_what_do_you_remember,
    "app": handle_open,
}

if __name__== "__main__":
   while True:
       query = takeCommand().lower()
       if "wake up" in query:
           greetme()

           while True:
               query = takeCommand().lower()
               if "go to sleep" in query:
                   speak("Ok sir , You can call me anytime")
                   break

               elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                         if sys.platform == "win32":
                             os.system("shutdown /s /t 1")
                         else:
                             speak("Shutdown command only supported on Windows.")
                    elif shutdown == "no":
                         break

               else:
                   # Find the matching command
                   for keyword, func in COMMANDS.items():
                       if keyword in query:
                           func(query)
                           break
