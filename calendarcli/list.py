import sys
from colorama import Style,Back, Fore

# print("list")

def data(a,o):
    if not not a:
        try :
            a = int(a)
            printXmonth(a)

        except Exception as e :
            if not (a in ("smsm")):
                print(Fore.YELLOW + f"-l{a} is not options!!" + Fore.RESET)
                sys.exit()
            else:
                if "m" in a : editMode()
                else : printStd()

    else:
        print("--list",o)
        if(('-m', '') in o or ('--modify', '')in o ):
            editMode()
        else:
            for i,j in o:
                if i == "-n":
                    try : printXmonth(int(j))
                    except Exception as e:
                        print(Fore.YELLOW + f"{j} is not a number. Please enter only number." + Fore.RESET)
                        sys.exit()
                else : print(Fore.YELLOW + f"{i} {j} is not option" + Fore.RESET)


def printXmonth(x):
    print(f"print {x} month")

def printStd():
    print("printSTD")

def editMode():
    print("printEdit")