import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import os
import sys
import smtplib
import psutil
import pyjokes
import pyautogui
from news import speak_news, getNewsUrl
from diction import translate
from loc import weather
from youtube import youtube
import psutil
import os
import getpass
import pyautogui



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)     # setting up new voice rate



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def listen():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        command = r.recognize_google(audio, language='en-in')
        print(f'User said: {command}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'None'
    return command


def init():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")

    else:
        speak('Good Evening ')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('path of folder you want to save/screenshot.png')


init()
while True:
    command = listen().lower()

    if 'wikipedia' in command:
        speak('Searching Wikipedia....')
        command = command.replace('wikipedia', '')
        results = wikipedia.summary(command, sentences=10)
        speak('According to Wikipedia')
        print(results)
        speak(results)

   
    if 'Alice are you there' in command:
        speak("Yes Sir, How can i help")

   

    elif 'explorer' in command:
        # Holds down the alt key
        pyautogui.keyDown("win")
        # Presses the tab key once
        pyautogui.press("e")
        # Lets go of the alt key
        pyautogui.keyUp("win")

    elif 'clear' in command:
        # Holds down the alt key
        pyautogui.keyDown("win")
        pyautogui.keyDown("cntrl")
        # Presses the tab key once
        pyautogui.press("right")
        # Lets go of the alt key
        pyautogui.keyUp("win")
        pyautogui.keyUp("cntrl")

    elif 'go to sleep' in command:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


    elif 'down' in command:

        pyautogui.press("down")

    elif 'open' in command:
        path='C:/'


        if "open" in command.lower():
            print("in open")       
            command=command.replace('open ','')     #Removing  open from String

            with open('paths.txt') as f:
                for line in f:
                    if command.lower() in line.lower():
                        a="start "+line #System command
                        print("start from a line")
                        os.system(a) #Opening the file


            for root,dirs,files in os.walk(path): #Lisiting all files
                
                for entry in files: #Looking through files
                    if command.lower() in entry.lower(): #comparing searched file with available files
                        response=listen()
                        speak("Did u mean "+entry)
                        if "yes" in response.lower():
                            
                            print(entry)  #print founded file
                            print("Opening"+root)
                            root=root.replace('C:/','C:/"')
                            root=root.replace('""','"') 
                            root=root+'"'
                            entry= '"'+entry+'"'
                            a=os.path.join(root,entry) #Getting a full path of the file
                            print(a) 
                            # a= "'"+'"'+a+'"'+"'"
                            # a=a.replace(' ','/') 
                            history = open('paths.txt', 'a')
                            history.write(a+"\n")
                            history.close()
                            a="start "+a #System command
                            print(a)
                            os.system(a) #Opening the file


    elif 'read' in command:

        pdfFileObject = open(command,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        count = pdfReader.numPages
        for i in range(count):
            page = pdfReader.getPage(i)
            speak(page.extractText())


    elif 'up' in command:

        pyautogui.press("up")

    elif 'left' in command:

        pyautogui.press("down")


    elif 'right' in command:

        pyautogui.press("up")


    elif 'screenshot' in command:
        speak("Yep")
        screenshot()


    elif 'the time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'Sir, the time is {strTime}')


    elif 'your master' in command:
            speak('Laison is my master')


    elif 'your name' in command:
        speak('My name is Alice')
    elif 'stands for' in command:
        speak('A.L.I.C.E stands for Automated Laison intelligent controll Entity')
   

    elif 'shutdown' in command:
            os.system('shutdown /p /f')
      

    elif 'cpu' in command:
        cpu()


    elif 'remember that' in command:
        speak("what should i remember sir")
        rememberMessage = listen()
        speak("you said me to remember"+rememberMessage)
        remember = open('data.txt', 'w')
        remember.write(rememberMessage)
        remember.close()

    elif 'do you remember anything' in command:
        remember = open('data.txt', 'r')
        speak("you said me to remember that" + remember.read())

    elif 'sleep' in command:
        sys.exit()

    elif 'dictionary' in command:
        speak('What you want to search in your intelligent dictionary?')
        translate(listen())


    elif 'email to' in command:
        try:
            command=command.replace('email to','')
            speak('What is the content?')
            content = listen()
            to = command
            sendEmail(to, content)
            speak('Email has been sent!')

        except Exception as e:
            speak('Sorry sir, Not able to send email at the moment')
