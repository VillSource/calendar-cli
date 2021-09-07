import getopt, sys,Document
import CalendarDisplay
import DataManager,CalendarManager


unixOptions = "had:e:sl:m"
gunOptions =[
    "help",
    "start",
    "user.name=",
    "add",
    "date=",
    "event=",
    "show",
    "list",
    "modify"
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

    while not not opts:
        o,a = opts.pop(0)
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
            sys.exit()
        elif o in ("--list", "-l"):
            CalendarDisplay.printEvent(opts,a)
            sys.exit()
        else:
            print(f"{o} is not option")





if __name__ == "__main__":
        main()

# pyinstaller --clean -y -n "Ccal" --add-data="data/*;data" Ccal.py
