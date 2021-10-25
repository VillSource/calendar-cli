from dataclasses import dataclass, asdict, field
from datetime import datetime
import os,sys, sqlite3
import julian

database = "schedule.db"
tables = "events"
today = datetime.today()

@dataclass
class Data:
    name:str
    uuid:str=''
    detail:str=''
    juliandate:float = field(default=0,init = False)

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
       
        try:
            self.connection = sqlite3.connect(getPath(database))
            a=list(self.connection.execute(f"""
                SELECT name FROM sqlite_master WHERE type='table' AND name='{tables}';
            """))

            if(not (tables,) in a): self.create_table()

        except Exception as e:print(e)


    def create_table(self):
        self.connection.execute(
            f'''
                create table {self.tables}(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    uuid TEXT,
                    name TEXT,
                    juliandate INTEGER,
                    detail TEXT
            );'''
        )

    
    def add(self,data:Data):
        command = f'''
            insert into {tables} {tuple( x  for x in asdict(data))} values {tuple( asdict(data)[x]  for x in asdict(data))};
        '''
        print(command)
        self.connection.execute(command)





if __name__ != "__main__":
    import pprint
    d = Database()
    a = Data("deksdflafjasdf","chaogal","de nada")
    pprint.pprint(a)
    # d.add(a)
    # d.connection.close()
    
