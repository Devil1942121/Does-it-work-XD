import pyaudio
import pyttsx3
from flask import Flask
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am sage. please tell me how may i help you")
 
 


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="YOUR_API_HERE"'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")



if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        if "open discord" in query:
            dpath = "C:\\Users\\user\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
            os.startfile(dpath)
            
        elif 'hi' in query or 'hello' in query:
            speak('Hello, how may I help you?')
        
        elif "open spotify" in query:
            spath = "C:\\Users\\user\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spath)

        elif "open command prompt" in query:
            cpath = "%windir%\\system32\\cmd.exe"
            os.system(cpath)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\user\\Desktop\\Jivan Book\\Songs"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))



        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open pinterest" in query:
            webbrowser.open("https://in.pinterest.com/")

        elif "open anime" in query:
            webbrowser.open("https://animepahe.org/")

        elif "open google" in query:
            speak(" what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+918638239726", "this is testing protocol",4,13)
            time.sleep(120)
            speak("message has been sent")

        elif "song on youtube" in query:
            kit.playonyt("Cradles")


        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
            
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22: 
                music_dir = 'C:\\Users\\user\\Desktop\\Jivan Book\\Songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
#to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
                   

        elif "tell me news" in query:
            speak("please wait, feteching the latest news")
            news()


        elif "email to bob" in query:
               
            speak("what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'schoolidjivan@gmail.com'
                password = 'Devil1942121' 
                send_to_email = 'deshmukhshivanirajendra@gmail.com'
                speak("okay, what is the subject for this email")
                query = takecommand().lower()
                subject = query  
                speak("and , what is the message for this email")
                query2 = takecommand().lower()
                message = query2 
                speak("please enter the correct path of the file into the shell")
                file_location = input("C:\\Users\\user\\Desktop\\Jivan Book\\Songs\\01 Cradles.mp3")

                speak("please wait,i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to bob")

            else:                
                email = 'schoolidjivan@gmail.com' 
                password = 'Devil1942121' 
                send_to_email = 'deshmukhshivanirajender@gmail.com' 
                message = query 
                server = smtplib.SMTP('smtp.gmail.com', 587) 
                server.starttls() 
                server.login(email, password) 
                server.sendmail(email, send_to_email , message) 
                server.quit() 
                speak("email has been sent to bob")