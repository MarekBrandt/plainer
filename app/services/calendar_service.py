from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import os

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_free_slots():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        raise Exception("File: token.json wasn't found. Authorize app.")

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.utcnow().isoformat() + 'Z'  # Format RFC3339
    end_time = (datetime.utcnow() + timedelta(days=7)).isoformat() + 'Z'

    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        timeMax=end_time,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    free_slots = []

    if events:
        current_time = datetime.utcnow()
        for event in events:
            start = datetime.fromisoformat(event['start'].get('dateTime', event['start'].get('date')))
            if current_time < start:
                free_slots.append({'start': current_time, 'end': start})
            current_time = datetime.fromisoformat(event['end'].get('dateTime', event['end'].get('date')))

        if current_time < datetime.fromisoformat(end_time.replace('Z', '')):
            free_slots.append({'start': current_time, 'end': datetime.fromisoformat(end_time.replace('Z', ''))})

    return free_slots
