import typer, sys,os
from datetime import datetime, timedelta
from monthdelta import monthdelta
from rich.console import Console
from rich import print
from .data.db import getPath, Data
from .data.google_calendar import Service

service = Service()
console = Console()
app = typer.Typer(add_completion=False)
state = { 'confirm' : False }

doc_events = typer.Argument(..., help='Enter event name',)
doc_dates = typer.Argument(
    str(datetime.today().date()),
    formats=[r"%Y-%m-%d"],
    help='Enter event date',
)
doc_details = typer.Option(False,'--detail','-d', help='Enter event details',show_default=False)
doc_location = typer.Option(False,'--place','-p', help='Enter event details',show_default=False)




@app.callback(invoke_without_command=True)
def _callback( 
    ctx: typer.Context, 
    confirm: bool = typer.Option(
        False,help="Confirm action",
        show_default=False)
):
    if(confirm):
        state['confirm'] = True
    # console.log(f'confirm : {state}')

    if(ctx.invoked_subcommand is None):
        list()
        sys.exit(1)


    
@app.command()
def add(
    event:str = doc_events,
    date:datetime = doc_dates,
    details:str = doc_details,
    location:str = doc_location,
):
    'Add your event to google calendar'
    event = Data(event, detail=details, location=location )
    event.start = date
    event.end = date+timedelta(hours=1)
    print(event)
    print(event.start,event.end)
    service.add_event(event)



@app.command()
def update(
    id:str = typer.Argument(None,help="Enter ID of event referance"),
    event:str = typer.Option(None,'--event','-e',help='Enter new event\'s name'),
    location:str = typer.Option(None,'--place','-p',help='Enter new event\'s location'),
    detail:str = typer.Option(None,'--detail','-d',help='Enter new event\'s detail')
):
    'description update func'
    print(event,location,detail)
    if not id:
        print('type "ccal list" to find event ID')
        return
    if not (event or location or detail):
        print('Please enter data to update or "ccal update --help"')
        return
    def callback(data):
        if event: data['summary'] = event
        if location: data['location'] = location
        if detail: data['description'] = detail
        return data
    print(service.update_event(id,callback,True))



@app.command()
def delete(
    id = typer.Argument(...,help='Enter Event\'s ID'),
):
    'description delete delete func'
    def callback(data):
        msg = ''
        msg += f"[red]{data['summary']}\n"
        try: msg += f"'Detail' : '{data['description']}'\n"
        except: pass
        try: msg += f"'Place'  : '{data['location']}'\n"
        except: pass
        console.print(msg,end='')
        if input('Do you want to delete this event [y,N] : ').upper() == 'Y':return True
        return False
    service.delete_event(id,callback)




@app.command()
def list(
    on_month:int = typer.Option(
        -1,
        help=f'Query events on month[1-12] and current year[{datetime.today().year}]',
        show_default=False
    ),
    date_start:datetime = typer.Option(
        str(datetime.today().replace(day=1).date()),
        formats=[r"%Y-%m-%d"],
        help='Query events start from this date'
    ),
    date_end:datetime = typer.Option(
        str((datetime.today().replace(day=1)+monthdelta(1)).date()),
        formats = [r'%Y-%m-%d'],
        help='Query events end to this date'
    ),
    modify:bool = typer.Option(False,'-m','--modify',show_default=False,help='List event then select to edit')
):
    'Query events from Google calendar'
    print(on_month)
    print(date_start)
    print(date_end)
    print(modify)

    if on_month<1:
        event:Data = service.list_events(dateMin = date_start, dateMax = date_end, RETURN=True)
    elif on_month>=1 and on_month<=12:
        date = datetime.now().replace(month=on_month,day=1,hour=0,minute=0,second=0)
        print('on month',date,'to',date+monthdelta(1))
        event:Data = service.list_events(dateMin = date, dateMax = date+monthdelta(1),RETURN=True)

    if event:
        for i in event:
            print(i.name, i.uuid)
    else:print('No events')
        






@app.command()
def login():
    'description login func'
    with console.status("[bold green]Working on tasks...") as status:
        service.login()
        console.log('Login completes.')


@app.command()
def logout():
    'description logout func'
    with console.status("[bold green]Delete token file...") as status:
        service.logout()
        console.log('Logout completes.')
                
        

@app.command()
def tmp():
    from .GUI import app
    app.start()
    # from .data.db import Database
    # from .data import google_calendar 




def main():
    app()




if __name__ == '__main__':
    main()