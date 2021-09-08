import datetime,re,sys
from colorama import Style,Back, Fore


def data(opt=[]):
    print(opt)
    date = datetime.datetime.today().date()
    event = str()
    
    for o,a in opt:
        if o in ("--event","-e"):
            event = a
        elif o in ("--date","-d"):
            if len(a)==10 and bool(re.match("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]",a)):
                date = a
            else:
                print(Fore.YELLOW + f"Date format {a} not match")
                print(f"Please enter in yyy-mm-dd such as {Back.MAGENTA} {date} "+Style.RESET_ALL)
                sys.exit()
        else:
            print(f"{o} is not option")
            sys.exit()
    try:
        if event:
            #  เพิ่ม fun ตรงนี้
            print(f"{Fore.GREEN}{event} on {date} has added to calendar!!{Fore.RESET}")
        else:
            print(Fore.YELLOW+'--add require option --event="<enter your event>"'+Fore.RESET)
    except Exception as e:
        print(f"Erroe -> {e}")