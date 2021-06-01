# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


import pyttsx3
import datetime
import wikipedia
import PyPDF2
import speech_recognition as sr
import os
import sys
import smtplib
import pyautogui
import os




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #select voice 0 male 1 female
engine.setProperty('rate', 175)     # setting up new voice rate



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    speak("Good Morning ")
elif hour >= 12 and hour < 18:
    speak("Good Afternoon ")

else:
    speak('Good Evening ')

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


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hello World")

        speak('Hello there')

        return []
