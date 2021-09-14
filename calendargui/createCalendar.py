import datetime
from calendar import monthrange
import re
import eel,sys

@eel.expose
def getDayList(date):
    try:
        diff = getDifDay(date)
        
    except :
        date = re.split((r'\D+'), date)

    diff = getDifDay(datetime.date(int(date[0]),int(date[1]),int(date[2])))

    data = list()
    if diff['current'][0] != 6:
        for i in range(diff['previous'][1]-diff['current'][0], diff['previous'][1]+1):
            data.append((i,'day day--disabled',''))

    for i in range(1,diff['current'][1]+1):
        data.append((i,'day',f'{int(date[0])}-{int(date[1])}-{i}'))

    if len(data)%7 != 0:
        for i in range(1,8-(len(data)%7)):
            data.append((i,'day day--disabled',''))

    return data

def getDifDay(date:datetime.date):
    cur = monthrange(date.year,date.month)
    try:
        prev = monthrange(date.year, date.month-1)

    except:
        prev = monthrange(date.year-1, 12)
    
    return {
        'current' : cur,
        'previous': prev
    }