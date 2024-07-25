import os
import re
from playsound import playsound
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import eel 

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
    
    # Standardize common application names
    app_dict = {
        "google chrome": "Google Chrome",
        "safari": "Safari",
        "firefox": "Firefox",
        "spotify": "Spotify",
        "notes": "Notes",
        "mail": "Mail",
        "male": "Mail",
        "calendar": "Calendar",
        "whatsapp": "WhatsApp",
        "maps": "Maps",
        "photos": "Photos",
        "dictionary": "Dictionary",
        "preview": "Preview",
        "siri": "Siri",
        "apple tv": "TV",
        "settings": "System Preferences", 
        "microsoft teams": "Microsoft Teams",
        "obsidian": "Obsidian",
        "sticker": "Stickies",
        "chess": "Chess",
        "clock": "Clock",
        "facetime": "FaceTime",
        "weather": "Weather",
        "anaconda": "Anaconda-Navigator",
        "v s code": "Visual Studio Code",
        "vs code": "Visual Studio Code",
        "virtual studio code": "Visual Studio Code",
        "pycharm": "PyCharm",
        "figma": "Figma",
    }

    if query in app_dict:
        app_name = app_dict[query]
        speak("Opening " + app_name)
        os.system('open -a "' + app_name + '"')
    else:
        speak("Application not found")
        print("Application not found: " + query)