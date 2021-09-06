"""
printCalendar
"""


from datetime import date
import calendar
import re
from colorama import Style,Back, Fore

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
    print("\n", re.sub(rday,rdayc,thisMonth))