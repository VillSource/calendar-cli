from check import isDate
from colorama import Style, Back, Fore
import sys, datetime

id = str()
oldEvent = str()
newEvent = str()
newDate = str()


def data(a, opt):
    global oldEvent
    global newDate
    global newEvent
    global id
    try:
        id = int(a)
    except Exception as e:
        oldEvent = a

    for i, j in opt:
        if i in ("--date", '-d'):
            if isDate(j):
                newDate = j
            else:
                print(Fore.YELLOW + f"Date format {a} not match")
                print(
                    f"Please enter in yyy-mm-dd such as {Back.MAGENTA} {datetime.datetime.today().date()} " + Style.RESET_ALL)
                sys.exit()
        elif i in ("--event", '-e'):
            newEvent = j
    print(id, oldEvent, "-->", newDate, newEvent)

    # updating...
    if oldEvent:
        pass
    else:
        pass
