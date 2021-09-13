import sys
from colorama import Style,Back, Fore
from calendarcli.dataManager import selectTableOnMounth
from datetime import datetime

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
        # print("--list",o)
        if(('-m', '') in o or ('--modify', '')in o ):
            editMode()
            sys.exit()

        else:
            for i,j in o:
                if i == "-n":
                    try : printXmonth(int(j))
                    except Exception as e:
                        print(Fore.YELLOW + f"{j} is not a number. Please enter only number." + Fore.RESET)

                elif i in ("--search","-s") :
                    search(j)

                else : print(Fore.YELLOW + f"{i} {j} is not option" + Fore.RESET)
                sys.exit()
                
            printStd()


d = datetime.today()

def search(event):
    from calendarcli.dataManager import searchEvent
    data = searchEvent(f"%{event}%")
    print("Search",event,"found",len(data))
    for i in data:
        print(f"  ├─{i}")
    print()

def printXmonth(x):
    fd = d
    for j in range(x):
        data = selectTableOnMounth(curDate=fd.date())
        for index,i in enumerate(data):
            if index == 0 :
                print("\n",f"{fd.strftime('%Y %B')}" )
            print(f"  ├─{i[2]} : {i[1]} (id:{i[0]})")
        try    : fd = datetime(int(fd.year), int(fd.month)+1, 1)
        except : fd = datetime(int(fd.year)+1, 1,1)
    print()


def printStd():
    print("\n",d)
    data = selectTableOnMounth()
    for i in data:
        print(f"  ├─{i[2]} : {i[1]} (id:{i[0]})")
    print()


def editMode():
    from pprint import pprint
    import inquirer

    l = list()
    r = list()
    for i in selectTableOnMounth():
        l.append(f"{i[2]} : {i[1]}")
        r.append(i)
    # print(l)

    questions = [
        inquirer.List('edit',
                        message="What event do you want to modify?",
                        choices=l,
                        carousel=True
                    ),
        
        inquirer.List('mode',
                        message="What do you want to do?",
                        choices=['Delete','Update'],
                        carousel=True
                    ),
    ]
    print(f"{d.strftime('%Y %B')}")
    answers = inquirer.prompt(questions)
    # pprint(answers)