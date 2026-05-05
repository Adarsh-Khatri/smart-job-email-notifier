import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('gmail', 'v1', credentials=creds)
    return service

# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# def authenticate_gmail():
#     creds = None

#     # Load existing token
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)

#     # If no valid creds → login
#     if not creds or not creds.valid:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             'credentials.json', SCOPES)
#         creds = flow.run_local_server(port=0)

#         # Save token
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     service = build('gmail', 'v1', credentials=creds)
#     return service


def get_emails(service, max_results=10):
    results = service.users().messages().list(
        userId='me', maxResults=max_results).execute()

    messages = results.get('messages', [])
    email_list = []

    for msg in messages:
        msg_detail = service.users().messages().get(
            userId='me', id=msg['id']).execute()

        payload = msg_detail['payload']
        headers = payload['headers']

        subject = ""
        sender = ""

        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
            if header['name'] == 'From':
                sender = header['value']

        email_list.append({
            "id": msg['id'],   # 🔥 IMPORTANT
            "subject": subject,
            "sender": sender
        })

    return email_list