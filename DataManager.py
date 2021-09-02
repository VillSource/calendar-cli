import sqlite3,sys,os,datetime

database = "data/schedule.db"

def getPath(filename):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundle_dir,filename))


def executeSQL(command):
    data =None
    try:
        with sqlite3.connect(getPath(database)) as con:
            data = con.execute(command)
    except Exception as e:
        print(f"Error ->{e}")
    return data


def creatTable(table):
    executeSQL(f'''
        create table {table}(
            event text,
            date real
        );
    ''')


def insertData(table,data,date=datetime.date.today()):
    executeSQL(f"""
        insert into {table} values("{data}",julianday({date}))
    """)

def selectTable(table):
    return executeSQL(f"""
        select * from {table}
    """)



# creatTable("Anirut")
# insertData("Anirut","bey")

# for row in selectTable("Anirut"):
#     print(row)