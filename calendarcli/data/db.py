from dataclasses import dataclass, asdict, field
from datetime import datetime
import os,sys, sqlite3
import julian
from rich import print

database = "schedule.db"
tables = "events"
today = datetime.today()

@dataclass
class Data:
    name:str
    uuid:str=''
    detail:str=''
    juliandate:float = field(default=julian.to_jd(today,fmt='jd'))

    @property
    def date(self):
      return julian.from_jd(self.juliandate, fmt='jd')
    
    @date.setter
    def date(self,v):
      try:
        self.juliandate = julian.to_jd(v, fmt='jd')
      except AttributeError:
        try:
          self.juliandate = julian.to_jd(datetime(v.year, v.month, v.day), fmt='jd')
        except AttributeError:
          self.juliandate = float(v)



def getPath(filename):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundle_dir, filename))



class Database:

    def __init__(self, database = database, tables = tables):        
        self.database = database
        self.tables = tables
        self.callback = None       
        try:
            with sqlite3.connect(getPath(database)) as connection:
                a=list(connection.execute(f"""
                    SELECT name FROM sqlite_master WHERE type='table' AND name='{self.tables}';
                """))
                if(not (self.tables,) in a): self.create_table().execute()
        except Exception as e:print(e)



    def execute(self):
        data = None
        try:
            with sqlite3.connect(getPath(database)) as con:
                data = con.execute(self.command)
        except Exception as e:
            print(f"Error ->{e}")
        if self.callback is not None:
            data = self.callback(data)
        self.command = None
        self.callback = None
        return data



    def create_table(self, table = None):
        if table is not None: self.tables = table
        self.command = f'''
            create table {self.tables}(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                uuid TEXT,
                name TEXT,
                juliandate INTEGER,
                detail TEXT
        );'''
        return self

    
    def add(self,data:Data):
        self.command = f'''
            insert into {self.tables} {tuple( x  for x in asdict(data))} values {tuple( asdict(data)[x]  for x in asdict(data))};
        '''
        return self

    @property
    def getall(self):
        self.command = f"select * from {self.tables}"
        def callback(data):
            datalist = []
            for i in list(data):
                tmp = Data(i[2],i[1],i[4],i[3])
                datalist.append(tmp)
            return datalist
        self.callback = callback
        return self





if __name__ == "__main__":
    import pprint
    d = Database()
    a = Data("deksdflafjasdf","chaogal","de nada")

    d.add(a).execute()
    print(d.getall.execute())
    
