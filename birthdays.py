"""Retrieves birthdays from Google contacts, and exports in various formats."""

import os.path
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from output import generate_output

SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']

TOKEN_FILE = "token.json"


def main():
    """Retrieve dates of birth using the People API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('people', 'v1', credentials=creds)

        # Call the People API, maximum 1000 contacts returned.
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=1000,
            personFields='names,birthdays').execute()
        connections = results.get('connections')

    except HttpError as err:
        print(err)
        sys.exit(1)

    birthdata = []

    # Go through all contacts, identifying only those with birthday data
    for person in connections:
        names = person.get('names')
        birthdays = person.get('birthdays')
        if names and birthdays:
            name = names[0].get('displayName')
            birthday = birthdays[0].get('date')
            if birthday != None:
                year = birthday.get('year')
                month = birthday.get('month')
                day = birthday.get('day')

                birthdata.append({"name": name, "year": year,
                                 "month": month, "day": day})

    # Sort the output in calendar order, starting with January.
    birthsorted = sorted(birthdata, key=lambda r: [
                         r[k] for k in ('month', 'day')])

    # Generate output files
    generate_output(birthsorted)


if __name__ == '__main__':
    main()
