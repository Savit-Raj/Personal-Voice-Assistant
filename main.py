import os
import eel
from engine.features import *
from engine.command import *

eel.init("frontend")

playAssistantSound()

os.system('open -a "Safari" "http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)