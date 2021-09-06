"""
จัดการกับฐานข้อมูล

"""

import sqlite3,sys,os,datetime

database = "data/schedule.db"

def getPath(filename):
    """
    รับเข้าชื่อไฟล์ที่อยู่ในโปรเจค
    ส่งออก full path เพื่อให้ใช้ได้เมื่อแปลงไฟล์เป็น .exe
    """
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundle_dir,filename))


def executeSQL(command=""):
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
            date text,
            jdat integer
        );
    ''')


def insertData(table,event,date):
    command =f"""
        insert into {table} values ("{event}",date("{date}"),julianday("{date}"))
    """
    executeSQL(command)
    # print(command + "\n"+date)

def selectTable(table):
    return executeSQL(f"""
        select * from {table}
    """)

def printDatabase(table):
    for i in selectTable(table):
        print(f"{i[0]}  -->  {i[1]}  -->  {i[2]}  -->  {jd_to_date(i[2])}")


def jd_to_date(jd):
    import math
    import datetime as dt
    jd = jd + 0.5
    
    F, I = math.modf(jd)
    I = int(I)
    
    A = math.trunc((I - 1867216.25)/36524.25)
    
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
        with open(getPath("data/.user.name"),'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error ->{e}")
def setUserName(name):
    try:
        with open(getPath("data/.user.name"),'w') as f:
            f.write(name)
    except Exception as e:
        print(f"Error ->{e}")



creatTable("event")
# insertData("event","start")

# for row in selectTable("Anirut"):
#     print(row)