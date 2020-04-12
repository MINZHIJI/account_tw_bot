from __future__ import print_function

import configparser

import pickle

import argparse,os

import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def config_file(string):
    if os.path.isfile(string):
        return string
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{string} is not a valid file")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('-f','--config_f', type=config_file, required=True, help="Config file path")
    return parser.parse_args()


# Parser the config file
parsed_args = parse_arguments()
config_dir = parsed_args.config_f
config = configparser.ConfigParser()
config.read(config_dir)
gapi_sheet_id = config['GAPI']['SPREADSHEET_ID']
gapi_sheet_scrects_file = config['GAPI']['SPREADSHEET_LIC']
oauth_scrects_file = config['OAUTH']['OAUTH_LIC']
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = gapi_sheet_id
SAMPLE_RANGE_NAME = 'Class!A:E'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                oauth_scrects_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s' % (row[0]))

if __name__ == '__main__':
    main()