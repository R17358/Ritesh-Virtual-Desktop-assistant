import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import cv2
import pyjokes
import pyautogui
import numpy as np
import requests
from bs4 import BeautifulSoup                                                   #web Srapping
from requests import get
import psutil                                                                   #battery
from googlesearch import search
from gnews import GNews
import pywhatkit
import wolframalpha
from tkinter import *
from PIL import Image,ImageTk
import threading
import subprocess

#wish
#date and time
#day
#note
#open facebook
#open twitter
#git hub
#stackoverflow
#voice command
#wikipedia
#youtube
#google
#amazon
#open command
#open code
#power left
#who are you,who made you
#location
#temperature
#screenshot
#shutdown and restart
#whatsapp
#question
#camera
#set alarm
#calculation
#joke
#switch window
#minimize or close
#other location
# what is "expert ans"
# play YT videos
# news
# search 
#exit









engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        print(f"good morning sir, its {tt}")
        speak(f"good morning sir, its {tt}")

    elif hour >= 12 and hour < 18:
        print(f"good afternoon sir, its {tt}")
        speak(f"good afternoon sir, its {tt}")

    else:
        print(f"good evening sir, its {tt}")
        speak(f"good evening sir, its {tt}")

    print("I am Jarvis Please tell me how may I help you?")
    speak("I am Jarvis Please tell me how may I help you?")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # it will take voice commands input from the microphone

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # when mic is listening our voice that time 1s gap can be okay
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said:{query}\n")

        except:
            # print(e)

            print("Say that again please...")
            speak("Say that again please")
            return "none"
        return query

def task():
    while True:
        query = takeCommand().lower()    
        if 'wikipedia' in query:
            try:

                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query,sentences=1)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except:
                pass
            
        elif "what is"  in query:
                try:
                    client = wolframalpha.Client("4Y594Q-5TAGRTVW86")
                    res = client.query(query)
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    speak("sorry , i don't have the answer for that ..")

        elif "news" in query:

            google_news = GNews()
            print("please tell me place:")
            speak("please tell me place:")
            place = takeCommand().lower()
            news = google_news.get_news(f"{place}")
            for i in range(1,4):

                print(f"{news[i]}")
                speak(f"{news[i]}")

        elif "where is" in query:
                        try:
                            query = query.replace("jarvis","")
                            query = query.replace("where is","")
                            location = query
                            reply_location = "Locating",location, " in google maps"
                            speak(reply_location)
                            webbrowser.open("http://www.google.com/maps/place/"+location)
                        except:
                            speak("unable to locate this place")
        
        elif "note" in query:
            speak("What should i write, sir")
            try:
                            note = takeCommand().lower()
                            file = open('jarvis.txt', 'w')
                            time_reply = " Should i include date and time"
                            speak(time_reply)
                            snfm = takeCommand().lower()
                            if 'yes' in snfm or 'sure' in snfm:
                                try:
                                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                                    file.write(strTime)
                                    file.write(" :- ")
                                    file.write(note)
                                except:
                                    speak("unable to write time in note, Sorry but note has been written without time")
                                    file.write(note)
                            else:
                                file.write(note)
            except:
                speak("unable to write note")

        elif "show notes" in query:
                        speak("Showing Notes")
                        file = open("jarvis.txt", "r")
                        speak(file.read())

        elif 'open youtube' in query:
                
            webbrowser.open_new_tab("youtube.com")
            speak("youtube opened")
            time.sleep(5)

        elif 'open facebook' in query:
                
            webbrowser.open_new_tab("facebook.com")
            speak("facebook opened")
            time.sleep(5)

        elif 'open twitter' in query:
                
            webbrowser.open_new_tab("twitter.com")
            speak("twitter opened")
            time.sleep(5)

        elif 'overflow' in query:
                
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("stackoverflow opened")
            time.sleep(5)
            
        elif 'w3school' in query:
                
            webbrowser.open_new_tab("https://www.w3schools.com/")
            speak("w3school opened")
            time.sleep(5)

        elif 'hub' in query:
                
            webbrowser.open_new_tab("https://github.com/")
            speak("github opened")
            time.sleep(5)

        elif 'open google' in query:
                
            webbrowser.open("google.com")
            speak("google opened")
            time.sleep(5)

        elif "shut down" in query:
            
            os.system("shutdown /s /t 5")

        elif "restart" in query:
            
            os.system("shutdown /r /t 5")

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            print("tell me time to set alarm")
            speak("tell me time to set alarm")
            try:
                s = takeCommand().lower()
                if nn == s:
                    speak("please wake up sir")
                
            except:
                pass

        elif "date" in query or "year" in query :
            date = datetime.datetime.now()
            

            print(f"today's date is {date}")
            speak(f"today's date is {date}")

        elif "day" in query :

            day = time.strftime("%A")
            print(f"today's day is {day}")
            speak(f"today's day is {day}")

        elif "calculation" in query:

            try:
                print("which calculation")
                speak("which calculation")
                m = takeCommand().lower()

                if "addition" in m or "sum" in m or "plus" in m:

                    try:
                        print("tell me first number")
                        speak("tell me first number")
                        a = takeCommand().lower()
                        print(a)

                        print("tell me second number")

                        speak("tell me second number")
                        b = takeCommand().lower()
                        print(b)
                        
                    except:
                       pass


                    c = int(a) + int(b)

                    print(f"sum is {c}")
                    speak(f"sum is {c}")


                elif "subtraction" in m or "difference" in m or "minus" in m:

                    try:
                        print("tell me first number")
                        speak("tell me first number")
                        a = takeCommand().lower()
                        print(a)
                        print("tell me second number")

                        speak("tell me second number")
                        b = takeCommand().lower()
                        print(b)

                    except:
                        pass


                    c = int(a) - int(b)

                    print(f"subtraction is {c}")
                    speak(f"subtraction is {c}")

                elif "multiply" in m or "multiplication" in m or "product" in m:

                    try:
                        print("tell me first number")
                        speak("tell me first number")
                        a = takeCommand().lower()
                        print(a)
                        print("tell me second number")

                        speak("tell me second number")
                        b = takeCommand().lower()
                        print(b)
                    except:
                        pass


                    c = int(a) * int(b)

                    print(f"multiply is {c}")
                    speak(f"multiply is {c}")

                elif "division" in m or "divide" in m:

                    try:
                        print("tell me first number")   
                        speak("tell me first number")
                        a = takeCommand().lower()
                        print(a)
                        print("tell me second number")

                        speak("tell me second number")
                        b = takeCommand().lower()
                        print(b)
                    except:
                        pass


                    c = float(a) / float(b)

                    print(f"divide is {c}")
                    speak(f"divide is {c}")

            except:
                pass
                    
        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "switch" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        #elif 'minimise' in query or 'background' or 'maximise' in query:
            #pyautogui.hotkey("win","w")

        #elif 'close' in query:
            #pyautogui.hotkey("ctrl","w")
            
        elif "power left" in query or "battery" in query:
            
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(f"sir our system have {percentage} percent battery")
            speak(f"sir our system have {percentage}% battery")

        elif "who are you" in query or "your name" in query or "yourself" in query:
            print("i am a virtual desktop assistant. myself jarvis.i am here to ease your computer related task")
            speak("i am a virtual desktop assistant. myself jarvis.i am here to ease your computer related task")

        elif "who developed you" in query or "who made you" in query:
            print("i am invented by a student as a mini project. their names are Harsh Dubey")
            speak("i am invented by a student as a mini project. their names are Harsh Dubey")

        elif "where i am" in query or "where we are" in query or "location" in query:
            print("wait sir, let me check")
            speak("wait sir, let me check")
            
            try:

                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                print(f"sir i am not sure, but i think we are in {city} city of {country} country")
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                print("sorry sir , Due to network issue i am not able to find our location")
                speak("sorry sir , Due to network issue i am not able to find our location")
                
        elif "screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img = cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
            cv2.imwrite(f"{name}.png",img)
            
            print("i am done sir, the screenshot is saved in our main folder")
            speak("i am done sir, the screenshot is saved in our main folder")

        elif "temperature" in query:
            print("at which location:")
            speak("at which location:")
            x = takeCommand().lower()
            search = f"temperature in {x}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f"current {search} is {temp}")
            speak(f"current {search} is {temp}")
                
        elif 'open amazon' in query:
                
            webbrowser.open("amazon.in")
            speak("amazon opened")
            time.sleep(5)
            
        elif 'open flipkart' in query:
            
            webbrowser.open("flipkart.com")
            speak("flipkart opened")
            time.sleep(5)
            
        elif 'time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S %p")
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\momin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("VS code opened")
            time.sleep(10)
            
        elif 'exit' in query or 'quit' in query or 'bye' in query:
            print("Okay bye sir I am deactivating ")
            speak("Okay bye sir I am deactivating ")
            exit()

        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("whatsapp opened")
            time.sleep(5)
               
        elif 'my question' in query:

            try:
                print("Yes sir  please wait ")
                speak("Yes sir please wait")
                cm = query.replace("my question","")
                url2 = f"https://www.google.com/search?q={cm}"
                n = requests.get(url2)
                data = BeautifulSoup(n.text,"html.parser")
                temp2 = data.find("div",class_="BNeawe").text
                print(f" {temp2}")
                speak(f"{temp2}")
                webbrowser.open(url2)
                time.sleep(3)
            except:
                pass

        elif 'search' in query:
            try:
                    
                print("please wait sir")
                speak("please wait sir")
                query = query.replace("search","")
                query = query.replace("about","")
                cm=query
                for j in search(cm,tld="co.in",num=5,pause=5,start=1,stop=1):
                    print(j)
                webbrowser.open(j)
            except:
                pass
            
        elif 'play' in query:
            try:
                
                query = query.replace("play","")
                pywhatkit.playonyt(query)
            except:
                pass

        elif "don't listen" in query or "wait" in query:
            print("tell me time for don't listening mode")
            speak("tell me time for don't listening mode")
            try:

                o = takeCommand().lower()
                time.sleep(int(o))
            except:
                pass

        elif 'open command' in query:
            os.system("start cmd")
            speak("command prompt opened")
            time.sleep(2)
            
        elif 'open camera' in query:
            cap= cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        else:
            print("I am not able to understand")
            speak("I am not able to understand")
        
def background(start):
        threading.Thread(target=start).start()

def background(task):
        threading.Thread(target=task).start()

def background(exit):
        threading.Thread(target=exit).start()



def gui():
    root = Tk()
    root.geometry("800x1000")
    root.configure(background="black")
    root.title("Virtual Desktop assistant")
   # root.wm_iconbitmap("download.svg")
    # root.attributes("-fullscreen",True)
    title = Label(text="WELCOME", bg="black", fg="white", padx="40",pady=1, font="Helvetica 29 bold")
    title.pack()
    f1 = Frame(root, borderwidth=0, bg="black", relief=SUNKEN)
    f1.pack(padx=0.5, pady=0.5)

    f2 = Frame(root, borderwidth=0, bg="black", relief=SUNKEN)
    f2.pack(padx=0.5, pady=0.5)

    b1 = Button(f1, fg="white", text="START", bg="black", bd="0", font="lucida 12 bold",
                command=lambda: background(start))
    b1.pack(padx=30, pady=50)

    b2 = Button(f1, fg="white", borderwidth=0, text="RERUN WITHOUT WISH", bg="black", font="lucida 12 bold",
                command=lambda: background(task))
    b2.pack(padx=40, pady=40)

    b3 = Button(f1, fg="white", text="EXIT", bg="black", bd="0", font="lucida 12 bold", command= quit)
    b3.pack(padx=90, pady=100)

    frameCnt = 20
    frames = [PhotoImage(file="jarvis.gif", format='gif -index %i' % (i)) for i in range(frameCnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)

    label = Label(f2, bd=0, highlightthickness=0)
    label.pack()
    root.after(0, update, 0)
    root.mainloop()

def start():
    wishMe()
    task()
if __name__ == "__main__":
    #wishMe()
    print("going..")
    gui()
          


    