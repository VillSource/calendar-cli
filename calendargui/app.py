import eel
import sys

eel.init('calendargui/web')

def start():
    print("start GUI...")
    print("Prase CLRL + C to stop.")
    eel.start('index.html')

@eel.expose
def printtext(s:str):
    print(s)