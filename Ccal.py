import getopt, sys,Document
from typing import Match
import CalendarDisplay
import DataManager,CalendarManager


unixOptions = "had:e:s"
gunOptions =[
    "help",
    "start",
    "user.name=",
    "add",
    "date=",
    "event=",
    "show"
]

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], unixOptions, gunOptions)
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    if len(opts)<1:
        CalendarDisplay.calendar()
        sys.exit()

    
    # for o, a in opts:
    #     # print(o)
    #     if o in ("-h", "--help"):
    #         Document.read_help_file()
    #         sys.exit()
    #     elif o in ("--start","-s"):
    #         print("Program is starting...")
    #         sys.exit()
    #     elif o in ("--user.name"):
    #         DataManager.setUserName(a)
    #         sys.exit()
    #     elif o in ("--date","-d"):
    #         print(running.date)
    #         running.date = a
    #         print(running.date)
    #     elif o in ("--event","-e"):
    #         print(running.event)
    #         running.event = a
    #         print(running.event)

    while not not opts:
        o,a = opts.pop(0)
        # print(o,a)
        if o in ("-h", "--help"):
            Document.read_help_file()
            sys.exit()
        elif o == "--start":
            print("Program is starting...")
            sys.exit()
        elif o in ("--user.name"):
            DataManager.setUserName(a)
            sys.exit()
        elif o in ("--add","-a"):
            CalendarManager.addEvent(opts)
            sys.exit()
        elif o in ("--show","-s"):
            DataManager.printDatabase("event")
        else:
            print("\n\n\n\n\n\n")





if __name__ == "__main__":
        main()

# pyinstaller --clean -y -n "Ccal" --add-data="data/*;data" Ccal.py
