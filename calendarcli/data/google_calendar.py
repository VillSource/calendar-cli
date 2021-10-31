from __future__ import print_function
import requests
# import datetime
from datetime import date, timezone, datetime, timedelta
from tzlocal import get_localzone_name
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from .db import getPath, Data, Database
from .setting import *
from rich import print
from .setting import *


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CNAME = getConfig('calendar', 'NAME')
CID = getConfig('calendar', 'ID')

database = Database()


class Service():

    def __init__(self, scopes=SCOPES):
        Service.SCOPES = scopes
        Service.token_file = getPath('token.json')
        Service.credentials_file = getPath('credentials.json')


    def login(self):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        creds = None
        if os.path.exists(Service.token_file):
            creds = Credentials.from_authorized_user_file( Service.token_file, Service.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    Service.credentials_file, Service.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(Service.token_file, 'w') as token:
                token.write(creds.to_json())

        self.service = build('calendar', 'v3', credentials=creds)
        self._newCalendar(CNAME)


    def logout(self):
        if os.path.exists(Service.token_file):
            os.remove(Service.token_file)

        else:
            print("You are not loged in.")



    def _calendar_list(self):
        page_token = None
        self.calendar = {}
        while True:
            item = self.service.calendarList().list(pageToken=page_token).execute()

            for calendar_list_entry in item['items']:
                self.calendar[calendar_list_entry['summary']
                              ] = calendar_list_entry['id']

            page_token = item.get('nextPageToken')

            if not page_token:
                break
        return self.calendar


    def _newCalendar(self, CNAME):
        clist = self._calendar_list()
        if(CNAME not in clist):
            self.service.calendars().insert(body={
                'summary': CNAME
            }).execute()


    def __isotime(time: datetime):
        if time:
            return time.replace(tzinfo=timezone.utc).isoformat()
        return None
    

    def __toDataclass(event):
        tmp = Data(event['summary'], event['id'])
        if 'location' in event:
            tmp.location = event['location']
        if 'description' in event:
            tmp.detail = event['description']
        if 'htmlLink' in event:
            tmp.htmllink = event['htmlLink']

        if 'dateTime' in event['start']:
            date = event['start']['dateTime']
            date = tuple([int(x) for x in date[:10].split('-')] +
                            [int(x) for x in date[11:-1].split(':')])
            tmp.start = datetime(*date)

            date = event['end']['dateTime']
            date = tuple([int(x) for x in date[:10].split('-')] +
                            [int(x) for x in date[11:-1].split(':')])
            tmp.end = datetime(*date)
        else:
            date = event['start']['date']
            tmp.start = datetime(*[int(x) for x in date.split('-')])
            date = event['end']['date']
            tmp.end = datetime(*[int(x) for x in date.split('-')])

        return tmp



    def list_events(self, dateMin: datetime = None, dateMax: datetime = None, RETURN=False,callback=None):
        self.login()
        dateMin = Service.__isotime(dateMin)
        dateMax = Service.__isotime(dateMax)
        if(RETURN):
            data = []
        page_token = None
        while True:
            events = self.service.events().list(
                calendarId=CID,
                timeMin=dateMin,
                timeMax=dateMax,
                pageToken=page_token,
            ).execute()
            for event in events['items']:
                tmp = Service.__toDataclass(event)
                if callback:
                    callback()
                    # database.add(tmp).execute()
                if(RETURN):
                    data.append(tmp)
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        if(RETURN):
            return data


    def add_event(self, data: Data):
        print(f"start : {data.start}")
        print(f"end   : {data.end}")
        tz = get_localzone_name()
        event = {
            'summary': data.name,
            'start': {
                'dateTime': data.start.astimezone().isoformat(),
                'timeZone': tz
            },
            'end':{
                'dateTime': data.end.astimezone().isoformat(),
                'timeZone': tz
            }
        }
        if data.location :
            event['location'] = data.location
        
        print(event)
        event = self.service.events().insert(calendarId=CID, body=event).execute()


    def update_event(self,id:str,confirm,RETURN=False):
        data = self.service.events().get(calendarId=CID, eventId=id ).execute()
        data = confirm(data)
        if data:
            updated_event = self.service.events().update(calendarId=CID, eventId=data['id'], body=data).execute()
        if RETURN:
            return Service.__toDataclass(data)


    def delete_event(self,id:str):
        self.service.events().delete(calendarId=CID, eventId=id).execute()





if __name__ == '__main__':
    print("google service")
    service = Service()

    a = Data('tme')
    a.start = datetime(2021,10,29)
    a.location = 'Home'
    service.add_event(a)
    # print(service.list_events(RETURN=False))
    # service.delete_event('3i02l4l32ngd24n2f4d4ls0chs')
    # def b(data):
    #     # print(data)
    #     data['summary'] = 'anirut'
    #     return data
    # print(service.update_event('63vkqhoq1n5p7rtcijei9p84jj',b,True))
