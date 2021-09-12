import sqlite3, sys, os, datetime
import calendar

database = "data/schedule.db"
tables = "event"


def getPath(filename):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundle_dir, filename))


def executeSQL(command=""):
    data = None
    try:
        with sqlite3.connect(getPath(database)) as con:
            data = con.execute(command)
    except Exception as e:
        print(f"Error ->{e}")
    return data


def creatTable(table=tables):
    try:
        with sqlite3.connect(getPath(database)) as con:
            data = con.execute(f'''
                create table {table}(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    event TEXT,
                    date TEXT,
                    jday INTEGER
                );''')
    except Exception as e:
        pass


def insertData(event, date, table=tables):
    command = f"""
        insert into {table} (event,date,jday) values ("{event}",date("{date}"),julianday("{date}"))
    """
    executeSQL(command)


def selectTable(table=tables):
    return executeSQL(f"""
        select * from {table}
    """)


def selectTableOrderByDate(direction="DESC", limit=0, table=tables):
    if limit > 0:
        limit = f"limit {limit}"
    else:
        limit = ""
    command = f"""SELECT * FROM {table} ORDER BY jday {direction} {limit}"""
    return executeSQL(command)


def selectTableOnMounth(curDate=datetime.datetime.now().date(), table=tables):
    end = datetime.datetime(
        curDate.year,
        curDate.month,
        calendar.monthrange(curDate.year, curDate.month)[1])
    command = f"SELECT * FROM {table} WHERE jday >= julianday('{curDate}') AND jday <= julianday('{end}')  ORDER BY jday"
    return executeSQL(command)


def printDatabase(table=tables):
    for i in selectTable(table):
        print(f"{i[0]} : {i[2]}  -->  {i[3]}  -->  {jd_to_date(i[3])}   -->  {i[1]}")


def jd_to_date(jd):
    import math
    import datetime as dt
    jd = jd + 0.5

    F, I = math.modf(jd)
    I = int(I)

    A = math.trunc((I - 1867216.25) / 36524.25)

    if I > 2299160:
        B = I + 1 + A - math.trunc(A / 4.)
    else:
        B = I

    C = B + 1524

    D = math.trunc((C - 122.1) / 365.25)

    E = math.trunc(365.25 * D)

    G = math.trunc((C - E) / 30.6001)

    day = C - E + F - math.trunc(30.6001 * G)

    if G < 13.5:
        month = G - 1
    else:
        month = G - 13

    if month > 2.5:
        year = D - 4716
    else:
        year = D - 4715
    return dt.datetime(int(year), int(month), int(day)).date()


def getUserName():
    try:
        with open(getPath("data/.user.name"), 'r') as f:
            return f.read()
    except FileNotFoundError as ef:
        name = input("Enter your name : ")
        setUserName(name)
        return name
    except Exception as e:
        print(f"Error ->{e}")


def setUserName(name):
    try:
        with open(getPath("data/.user.name"), 'w') as f:
            f.write(name)
    except Exception as e:
        print(f"Error ->{e}")


creatTable()
# insertData("event","start")

# for row in selectTable("Anirut"):
#     print(row)
