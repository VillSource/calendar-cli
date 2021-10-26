import typer, sys,os
from datetime import datetime
from time import sleep
from rich.console import Console
from .data.db import getPath

console = Console()
app = typer.Typer(add_completion=False)
state = {
    'confirm' : False
}

doc_events = typer.Argument(...,
    help='Enter event name or event id',
)
doc_dates = typer.Argument(
    datetime.today().date(),
    formats=["%Y-%m-%d"],
    help='Enter event date',
)






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
    event = doc_events,
    date:datetime = doc_dates
):
    'description add func'
    print("add")

@app.command()
def update(
    event = doc_events,
):
    'description update func'
    print("update")

@app.command()
def delete(
    event = doc_events,
):
    'description delete delete func'
    print("delete")

@app.command()
def list():
    'description list func'
    print("list")





from .data.google_calendar import Service
service = Service()

@app.command()
def login():
    'description login func'
    with console.status("[bold green]Working on tasks...") as status:
        service.login()
        console.log('completes.')


@app.command()
def logout():
    'description logout func'
    with console.status("[bold green]Delete token file...") as status:
        service.logout()
                
        

@app.command()
def tmp():
    # from .data.db import Database
    from .data import google_calendar 
    # console.print(service.calendar_list())



def main():
    app()




if __name__ == '__main__':
    main()