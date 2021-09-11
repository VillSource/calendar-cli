import sys
import getopt

unixOptions = "hau:d:l:me:"
gunOptions =[
    "help",
    "add",
    "date=",
    "event=",
    "update=",
    "delete=",
    "list",
    "modify"
]

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], unixOptions, gunOptions)
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    try : o,a = opts.pop(0)
    except (IndexError) as e : o="calendar"

    if o in ("--help","-h"):
        import help
    elif o in ("--add","-a"):
        import add
        add.data(opts)
    elif o in ("--update","-u"):
        import update
        update.data(a,opts)
        print("update")
    elif o in ("--delete","-d"):
        print("delete")
    elif o in ("--list","-l"):
        print("list")
    elif o == "calendar":
        import icalendar
        icalendar.printCalendar()
    else:import help


if __name__ == '__main__':
    main()
