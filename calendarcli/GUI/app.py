import eel
from ..data.db import getPath
from datetime import datetime , timedelta
from monthdelta import monthdelta 
from ..data.google_calendar import Service

from rich import print
from rich.console import Console
console = Console()

eel.init(getPath('../GUI/web'))

def start():
    print("start GUI...",'\n','web')
    print("Prase CLRL + C to stop.")
    print(eel.root_path)
    eel.start('index.html')


@eel.expose
def getEventSourcesGoogle(year:int, month:int):
    service = Service()
    startMonth = datetime(year,month,1)
    endMonth = startMonth + monthdelta(1)
    with console.status('[green]Downdload events from Google Calendar...'):
        events = service.list_events( dateMin=startMonth, dateMax=endMonth, RETURN=True)
        eventSources = []
        for i in events:
            tmp = {}
            tmp['title'] = i.name
            tmp['description'] = i.detail
            tmp['start'] = i.start.isoformat()
            tmp['end'] = i.end.isoformat()
            tmp['allDay'] = i.start + timedelta(hours=24) == i.end 
            eventSources.append(tmp)
        eel.addEventToCalendar(eventSources)
    console.log('Get Event Sources done')
    # print(eventSources)
    


if __name__ == '__main__':
    start()