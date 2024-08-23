import eel
import os

from engine.features import *
from engine.command import *

def start():
    eel.init("frontend")

    playAssistantSound()

    os.system('open -a "Google Chrome" "http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)
