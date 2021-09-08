from os import path
import sys



unixOptions = "hau:d:l:"
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
    arg = sys.argv[1:]    
    o = arg.pop(0)

    if o in ("--help","-h"):
        import calendarcli.help
    elif o in ("--add","-a"):
        print("add")
    elif o in ("--update","-u"):
        print("update")
    elif o in ("--delete","-d"):
        print("delete")
    elif o in ("--list","-l"):
        print("list")
    else:import calendarcli.help


if __name__ == '__main__':
    main()
