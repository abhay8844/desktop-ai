import pyttsx3
import speech_recognition 
import wikipedia
import requests
import os
import plyer 
from bs4 import BeautifulSoup
import datetime
import pyautogui
import random
import speedtest



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
    os.startfile("alarm.py")

if __name__== "__main__":
   while True:
       query = takeCommand().lower()
       if "wake up" in query:
           from GreetMe import greetme
           greetme()

           while True:
               query = takeCommand().lower()
               if "go to sleep" in query:
                   speak("Ok sir , You can call me anytime")
                   break
                
      


#########################################################################################    
               
               elif "hello" in query:
                    speak("Hello sir, how are you ?")
               elif "i am fine" in query:
                    speak("that's great, sir")
               elif "how are you" in query:
                    speak("Perfect, sir")
               elif "thank you" in query:
                    speak("you are welcome, sir")
               elif "introduce yourself" in query:
                    speak("I'm zira, your personal AI assistant, here to help with a wide range of tasks like answering questions, ")     

               elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
               elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
               elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

               elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
               elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

               elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")   

               elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

               elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("screenshort.jpg")


               elif "take my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("space")  
                           
               elif "close camera" in query:
                    pyautogui.hotkey("ctrl","w")            

               elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
               elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

               if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "wikipedia")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

               elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

               elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)  

               elif "whatsapp" in query:
                         from Whatsapp import sendMessage
                         sendMessage()   

               elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)
                                                     
               elif "temperature" in query:
                    search = "temperature is belgaum "
                    url = f"https://www.google.com/search?q={search}" 
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
               
               elif "weather" in query:
                    search = "weather in belgaum"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

               elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

               elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

               elif "date" in query:
                    strTime = datetime.datetime.now().strftime("%d:%m")    
                    speak(f"Sir, today date is {strTime}")

               elif "finally sleep" in query:
                    speak("going to sleep, sir,if you have any questions please weak me up, i am ready to help you again, sir")
                    exit()

               elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()

               elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to " + remember.read()
                          )
               elif "app" in query:
                    query = query.replace("open", "")
                    query = query.replace("app", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

               
               elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                         os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                         break