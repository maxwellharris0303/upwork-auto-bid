from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1T2V1pUAEK9lnFlq1RA7A-ZHVTAvwGlmtAvfvaZ41a_s'
SAMPLE_RANGE_NAME = 'upwork profile!A1:E'


profileData = []

profileEmail = []

profileStatus = []

contactInfo = []

columnCount = 0

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        profileData.clear()
        profileEmail.clear()
        profileStatus.clear()
        contactInfo.clear()
        # print('Property Address, City:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            if len(row) >= 2:
                profileData.append('%s, %s' % (row[0], row[1]))
                profileEmail.append('%s' % (row[0]))
            if len(row) >= 5:
                profileStatus.append('%s' % (row[4]))
            else:
                profileStatus.append('Available')
            if len(row) >= 4:
                contactInfo.append('%s' % (row[3]))
            else:
                contactInfo.append('No')

        print(getContactInfo())
    except HttpError as err:
        print(err)

def getProfileData():
    return profileData

def getProfilesEmail():
    return profileEmail

def getProfileStatus():
    return profileStatus

def getContactInfo():
    return contactInfo

def getColumnCount():
    columnCount = len(profileData)
    return columnCount

def insertData(range_name_email, email, range_name_created_time):
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    values_email = [
        [email]
    ]
    values_created_time = [
        [current_datetime]
    ]
    request_body_email = {
        'values': values_email
    }
    request_body_created_time = {
        'values': values_created_time
    }

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Finally, call the API to write the data to the spreadsheet
        result = service.spreadsheets().values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=range_name_email,
                valueInputOption='USER_ENTERED',
                body=request_body_email
            ).execute()
        result1 = service.spreadsheets().values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=range_name_created_time,
                valueInputOption='USER_ENTERED',
                body=request_body_created_time
            ).execute()

        print('{0} email created.'.format(result.get('updatedCells')))
        print('{0} time created.'.format(result1.get('updatedCells')))
    except HttpError as err:
        print(err)

def insertBidStatusData(range_name, bid_amount):

    values_bid = [
        [f'Auto bid({bid_amount})']
    ]
    request_body = {
        'values': values_bid
    }


    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Finally, call the API to write the data to the spreadsheet
        result = service.spreadsheets().values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=range_name,
                valueInputOption='USER_ENTERED',
                body=request_body
            ).execute()

        print('{0} bid status updated.'.format(result.get('updatedCells')))
    except HttpError as err:
        print(err)

def insertContactInfo(range_name, contact_info):

    if contact_info == "Contact":
        values_contact_info = [
            ['Contact!!!']
        ]
    else:
        values_contact_info = [
            ['No']
        ]
    request_body = {
        'values': values_contact_info
    }


    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Finally, call the API to write the data to the spreadsheet
        result = service.spreadsheets().values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=range_name,
                valueInputOption='USER_ENTERED',
                body=request_body
            ).execute()

        print('{0} contact info updated.'.format(result.get('updatedCells')))
    except HttpError as err:
        print(err)
def insertProfileStatus(range_name, status):

    # if status == "Action Required":
    #     values_profile_status = [
    #         ['Contact']
    #     ]
    # else:
    #     values_profile_status = [
    #         ['No']
    #     ]
    values_profile_status = [
        [status]
    ]
    request_body = {
        'values': values_profile_status
    }


    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Finally, call the API to write the data to the spreadsheet
        result = service.spreadsheets().values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range=range_name,
                valueInputOption='USER_ENTERED',
                body=request_body
            ).execute()

        print('{0} profile status updated.'.format(result.get('updatedCells')))
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()