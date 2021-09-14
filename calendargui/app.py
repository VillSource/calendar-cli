import eel
import sys
from calendargui.createCalendar import getDayList as getday

eel.init('calendargui/web')

def start():
    print("start GUI...")
    print("Prase CLRL + C to stop.")
    eel.start('index.html',disable_cache=True,)

@eel.expose
def printtext(s:str):
    print(s)
# @eel.expose
# def getDayList(date):
#     return getday(date)