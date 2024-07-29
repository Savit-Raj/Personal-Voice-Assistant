import os
import re
import sqlite3
import struct
import time
import pvporcupine
import webbrowser
import pyautogui
from playsound import playsound
import pyaudio
import urllib3
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import eel
from engine.helper import *
import subprocess
from urllib.parse import quote

con = sqlite3.connect("voyage.db")
cursor = con.cursor()

# Assistant Sound
@eel.expose
def playAssistantSound():
    music_dir = "frontend//assets//audio//start_sound.mp3"
    playsound(music_dir)


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube.")
        kit.playonyt(search_term)
    else:
        speak("Sorry, didn't get you.")
        eel.DisplayMessage("Sorry, didn't get you.")


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


def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # Replace with your Picovoice access key
        access_key = "6YYG0Mqx/LjqKTlM6OiHUWdYud9snGY+e8HOa7C3CVd2HvKz9msFqA=="

        # Replace with the path to your custom .ppn file
        porcupine = pvporcupine.create(
            access_key=access_key,
            keyword_paths=["engine/Hey_Voyage.ppn"]
        )

        paud = pyaudio.PyAudio()

        # Audio stream setup
        audio_stream = paud.open(rate=porcupine.sample_rate,
                                 channels=1,
                                 format=pyaudio.paInt16,
                                 input=True,
                                 frames_per_buffer=porcupine.frame_length)

        # Loop for streaming
        while True:
            try:
                # Read audio data
                keyword = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
                keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

                # Process keyword
                keyword_index = porcupine.process(keyword)

                # Check if the keyword is detected
                if keyword_index >= 0:
                    print("hotword detected")

                    # Pressing shortcut key 'v'
                    pyautogui.press("v")
                    time.sleep(2)
            except IOError as e:
                if e.errno == -9981:
                    print("Input overflowed. Skipping frame...")
                else:
                    raise
            except Exception as e:
                print(f"An unexpected error occurred while processing audio: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video', 'please']
    query = removeWords(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()

        mobile_no_str = str(results[0][0])
        if not mobile_no_str.startswith('+91'):
            mobile_no_str = '+91' + mobile_no_str
        return mobile_no_str, query
    
    except:
        speak('Contact Does not Exist please')
        return '0' , '0'
    

def whatsApp(mobile_no, message, flag, name):

    if flag == 'whatsapp':
        encoded_message = quote(message)
        whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
        full_command = f'open "{whatsapp_url}"'
        subprocess.run(full_command, shell=True)
        time.sleep(1)
        os.system('osascript -e \'tell application "System Events" to keystroke return\'')
        eel.DisplayMessage("Message sent to "+ name)
        speak("Message sent to "+ name)

    else:
        if flag == 'video':
            eel.DisplayMessage(f"Video calling {name}")
            speak(f"Video calling {name}")
            whatsapp_url = f"whatsapp://send?phone={mobile_no}"

        else:
            eel.DisplayMessage(f"Calling {name}")
            speak(f"Calling {name}")
            whatsapp_url = f"whatsapp://send?phone={mobile_no}"
            print(whatsapp_url)

        full_command = f'open "{whatsapp_url}"'
        subprocess.run(full_command, shell=True)
