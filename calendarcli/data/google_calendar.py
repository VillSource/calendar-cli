from __future__ import print_function
import datetime
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

CNAME = getConfig('calendar','NAME')
CID = getConfig('calendar','ID')

database = Database()

class Service():


    def __init__(self, scopes = SCOPES):
        Service.SCOPES = scopes
        Service.token_file = getPath('token.json')
        Service.credentials_file = getPath('credentials.json')
        self._newCalendar(CNAME)


    def login(self):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(Service.token_file):
            creds = Credentials.from_authorized_user_file(Service.token_file, Service.SCOPES)
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



    def logout(self):
        if os.path.exists(Service.token_file):
            os.remove(Service.token_file)

        else: 
            print("You are not loged in.")



    def _calendar_list(self):
        self.login()
        page_token = None
        self.calendar = {} 
        while True:
            item = self.service.calendarList().list(pageToken=page_token).execute()

            for calendar_list_entry in item['items']:
                self.calendar[calendar_list_entry['summary']] = calendar_list_entry['id']

            page_token = item.get('nextPageToken')
            
            if not page_token:
                break
        return self.calendar


    def _newCalendar(self,CNAME):
        clist = self._calendar_list()
        if(CNAME not in clist):
            self.service.calendars().insert(body={
                'summary': CNAME
            }).execute()


    def download(self):
        self.login()
        page_token = None
        while True:
            events = self.service.events().list(calendarId=CID, pageToken=page_token).execute()
            for event in events['items']:
                tmp = Data(event['summary'],event['id'])
                database.add(tmp).execute()
            page_token = events.get('nextPageToken')
            if not page_token:
                break
    

    


if __name__ != '__main__':
    print("google service")
    service = Service()
    service.download()