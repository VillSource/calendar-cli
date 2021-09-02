import getopt, sys,os,DataManager


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

    # print(opts)

    
    for o, a in opts:
        if o in ("-h", "--help"):
            read_help_file()
            sys.exit()
        elif o == "--start":
            print("Program is starting...")
        # else:
        #     assert False, "unhandled option"



def read_help_file():
    import codecs
    with codecs.open(DataManager.getPath('data/Document.txt'), encoding='utf-8') as help_file:
       print(help_file.read())



if __name__ == "__main__":
    main()


# pyinstaller --clean -y -n "Ccal" --add-data="data/*;data" Ccal.py