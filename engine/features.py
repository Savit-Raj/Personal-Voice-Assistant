import os
import re
import sqlite3
import webbrowser
from playsound import playsound
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import eel 

con = sqlite3.connect("voyage.db")
cursor = con.cursor()

# Assistant Sound
@eel.expose
def playAssistantSound():
    music_dir = "frontend//assets//audio//start_sound.mp3"
    playsound(music_dir)

def extract_yt_term(command):
    # To find song
    pattern = r'(?:play\s+)?(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube.")
        kit.playonyt(search_term)
    else:
        speak("Sorry, didn't get you.")
        eel.DisplayMessage("Sorry, didn't get you.")


def extract_g_term(command):
    # To search name
    pattern = r'(?:search\s+)?(.*?)\s+on\s+google'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

def SearchGoogle(query):
    search_term = extract_g_term(query)
    if search_term:
        speak("Googling " + search_term + ".")
        kit.search(search_term)
    else:
        speak("Sorry, didn't get you.")
        eel.DisplayMessage("Sorry, didn't get you.")

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").lower().strip()

    if open != "":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)',(query,)
            )
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.system('open -a "' + results[0][0] + '"')

            elif len(results) == 0:
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)',(query,)
                )
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening "+query)
                    eel.DisplayMessage("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("URL not found.")
                    eel.DisplayMessage("URL not found.")

        except:
            speak("Path or URL not in database.")
            eel.DisplayMessage("Path or URL not in database.")