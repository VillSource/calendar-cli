import eel
from ..data.db import getPath, Data
from datetime import datetime , timedelta
from monthdelta import monthdelta 
from ..data.google_calendar import Service
from tzlocal import get_localzone_name, get_localzone

from rich import print
from rich.console import Console
console = Console()

service = Service()
eel.init(getPath('../GUI/web'))

def start():
    print("start GUI...",'\n','web')
    print("Prase CLRL + C to stop.")
    print(eel.root_path)
    eel.start('index.html')


@eel.expose
def getEventSourcesGoogle(year:int, month:int,date:int):
    eel.loadingProgressBarShow()
    start = datetime(year,month,date)
    end = start + monthdelta(1)
    start -= timedelta(days=15)
    with console.status('[green]Downdload events from Google Calendar...'):
        events = service.list_events( dateMin=start, dateMax=end, RETURN=True)
        eventSources = []
        for i in events:
            tmp = {}
            tmp['GoogleCalendarUrl'] = i.htmllink
            tmp['title'] = i.name
            tmp['description'] = i.detail
            tmp['start'] = i.start.isoformat()
            tmp['end'] = i.end.isoformat()
            tmp['allDay'] = i.start + timedelta(hours=24) == i.end 
            tmp['guuid'] = i.uuid
            eventSources.append(tmp)
        eel.addEventToCalendar(eventSources)
    eel.loadingProgressBarHide()
    console.log('Get Event Sources done')

@eel.expose
def moveEventGoogle(id:str,start:str, end:str, allDay:bool):
    eel.loadingProgressBarShow()
    if not end:
        end = f'{start[:4]}-{start[5:7]}-{start[8:10]}'
        end = datetime(*[int(x) for x in end.split('-')])
        if allDay:
            end += timedelta(hours=24)
            end = end.isoformat()
            end = end[:10]
        else:
            end += timedelta(hours=int(start[11:13])+1)
            print(start[11:13])
            end = end.isoformat()
    with console.status(f'[green]{id} move to {start}||{end}'):
        def a(a):
            if a:
                if allDay:
                    a['start']={'date':start},
                    a['end']={'date':end}
                else:
                    a['start']={
                        'dateTime':start+'Z',
                        'timeZone':get_localzone_name()
                    }
                    a['end']={
                        'dateTime':end+'Z',
                        'timeZone':get_localzone_name()
                    }
                return a
        service.update_event( id,a)
    eel.loadingProgressBarHide()
    console.log('Updated.')

def __to_date(data):
    # 11/01/2021 07:00 am
    tmp =([
        int(x) for x in data[:10].split('/')
    ])
    return datetime(tmp[2],tmp[0],tmp[1])

def __to_datetime(data):
    tmp = __to_date(data[:10])+timedelta()
    hours = int(data[11:13])%12
    minute = int(data[14:16])
    type = data[17:19]
    if type =='pm':hours+=12
    return tmp.replace(hour=hours,minute=minute)

@eel.expose
def addEventGoogle(data:dict):
    event = Data(data['name'],detail=data['desc'],location=data['location'])
    event.start = __to_date(data['date'])
    if data['allDay'] == 'true':
        event.end = event.start + timedelta(hours=24)
    else:
        event.start = __to_datetime(data['date'][:19])
        if len(data['date'])>=22: event.end   = __to_datetime(data['date'][22:])
        else:event.end = event.start + timedelta(hours=1)
    # print(event)
    # print(event.start)
    # print(event.end)
    service.add_event(event)
    
    
@eel.expose
def log(*args):
    msg = ''
    for i in args:
        msg += i.__str__()+' '
    console.log(msg)

if __name__ == '__main__':
    start()