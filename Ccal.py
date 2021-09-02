import getopt, sys,os,DataManager
from colorama import Style,Back
import CalendarDisplay


unixOptions = "hv:"
gunOptions =[
    "help",
    "start",
]

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], unixOptions, gunOptions)
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    
    for o, a in opts:
        if o in ("-h", "--help"):
            read_help_file()
            sys.exit()
        elif o == "--start":
            print("Program is starting...")
            sys.exit()
        # else:
        #     assert False, "unhandled option"
        
    CalendarDisplay.calendar()



def read_help_file():
    import codecs
    with codecs.open(DataManager.getPath('data/Document.txt'), encoding='utf-8') as help_file:
       print(help_file.read())



if __name__ == "__main__":
    main()


# pyinstaller --clean -y -n "Ccal" --add-data="data/*;data" Ccal.py