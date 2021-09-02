import sqlite3,sys,os

database = "data/schedule.db"

def getPath(filename):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundle_dir,filename))


def executeSQL(command):
    try:
        with sqlite3.connect(getPath(database)) as con:
            con.execute(command)
    except Exception as e:
        print(f"Error ->{e}")
        

def creatTable(table):
    executeSQL(f'''
        create table {table}(
            event text,
            date real
        );
    ''')




creatTable("Anriut")