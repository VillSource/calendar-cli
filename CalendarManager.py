from datetime import datetime
import re,sys
from colorama import Style,Back, Fore
import DataManager

dataTable = "event"

def addEvent(args=[]):
    event = str()
    date = str(datetime.now().date())

    for o,a in args:
        if o in ("--event","-e"):
            event = a
        elif o in ("--date","-d"):
            if bool(re.match("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]",a)):
                date = a
            else:
                print(Fore.YELLOW + f"date format {date} not match")
                print(f"Please enter in yyy-mm-dd such as {Back.MAGENTA} {datetime.now().date()} "+Style.RESET_ALL)
                sys.exit()
        else:
            print(f"{o} is not option")
            sys.exit()

    try:
        DataManager.insertData(dataTable,event,date)
        print(f"{Fore.GREEN}{event} on {date} has added to calendar!!{Fore.RESET}")
    except Exception as e:
        print(f"Erroe -> {e}")
    
    