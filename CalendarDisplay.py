"""
printCalendar
"""


from datetime import date, datetime
import calendar,DataManager
import re
from colorama import Style,Back, Fore
from CalendarManager import dataTable
import inquirer


today = date.today()
year  = today.year
month = today.month
thisMonth = calendar.month(year,month)

def calendar():
    """
    print calendar highlighted current day
    """
    date  = today.day.__str__().rjust(2)
    rday  = ('\\b' + date + '\\b').replace('\\b ', '\\s')
    rdayc = Back.GREEN+ Fore.BLACK + date + Style.RESET_ALL
    print(f"\n", re.sub(rday,rdayc,thisMonth))
    print(f"Hello {DataManager.getUserName()} : {today}\n")

def printEvent(arg,a):
    # print(arg,a)
    data = DataManager.selectTableOnMounth(dataTable)
    choice = str()
    for i in data:
        choice = choice + f"{i[2]}  :  {i[1]}\n"

    if ((not not a) and a[0] == 'm') or ((not not arg) and arg[0][0] in ('-m','--modify')):
        questions = [
            inquirer.List('event',
                            message="Which event do you want to modify?",
                            choices=choice.split("\n")[:-1],
                            carousel=True
                        ),
            inquirer.List('edit',
                            message="What do you want to do with ?",
                            choices=["Update","Delete",],
                            carousel=True
                        )
        ]
        answers = inquirer.prompt(questions)
        print(answers)
    else:print(choice)