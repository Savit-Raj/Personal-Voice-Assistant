from gtts import gTTS
import speech_recognition as sr
import os
import eel
import time

def speak(text):
    text = str(text)
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("afplay output.mp3")  # Use afplay to play the audio on macOS
        eel.DisplayMessage(text)
        eel.receiverText(text)
    else:
        print("No text to speak")
        eel.DisplayMessage("No text to speak")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        eel.DisplayMessage('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, 10, 6)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            eel.DisplayMessage("Sorry, Didn't get you.")
            speak("Sorry, Didn't get you.")
            eel.ToggleVisibility()
            return ""

    
    try:
        print("Recognizing....")
        eel.DisplayMessage('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        eel.DisplayMessage("Service request error")
        speak("Sorry, can not help.")
        eel.ToggleVisibility()
        return ""
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        eel.DisplayMessage("Sorry, Could not understand you")
        speak("Sorry, Could not understand you.")
        eel.ToggleVisibility()
        return ""
    except Exception as e:
        print(f"Error: {str(e)}")
        eel.DisplayMessage("An error occurred")
        speak("Sorry, can not help.")
        
        eel.ToggleVisibility()
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message = 1):

    if message ==1:
        query = takeCommand()
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "on google" in query:
            from engine.features import SearchGoogle
            SearchGoogle(query)

        elif "call" in query:
            from engine.features import findContact
            from engine.features import whatsApp
            if 'video call' in query:
                message = 'video'
                contact_no, name = findContact(query)
                if contact_no != '0':
                    whatsApp(contact_no, query, message, name)
                else:
                    eel.DisplayMessage("Contact not found")
                    speak("Contact not found")
            else:
                message = 'voice'
                contact_no, name = findContact(query)
                if contact_no != '0':
                    whatsApp(contact_no, query, message, name)
                else:
                    eel.DisplayMessage("Contact not found")
                    speak("Contact not found")

        elif "whatsapp" in query:
            from engine.features import findContact
            from engine.features import whatsApp
            message = 'whatsapp'
            contact_no, name = findContact(query)
            if contact_no != '0' and name!= '0':
                eel.DisplayMessage("Please speak the Whatsapp message.")
                speak("Please speak the Whatsapp message.")
                query = takeCommand()
                speak("Whatsapping "+name)
                whatsApp(contact_no, query, message, name)
                
            else:
                speak("Contact not found")

        else:
            from engine.features import chatBot
            chatBot(query)

    except Exception as ee:
        print(ee)

    eel.ShowHood()