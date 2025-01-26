from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone

from app.auth.google_auth import get_credentials


def get_free_slots() -> list[dict[str, datetime]]:
    now = datetime.now(timezone.utc)
    end_time = (now + timedelta(days=7))

    events = get_all_events(now, end_time)

    return find_free_slots(events, now, end_time)


def get_all_events(start_time: datetime, end_time: datetime):
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    result = service.events().list(calendarId='primary', orderBy='startTime', singleEvents=True,
                                   timeMin=start_time.isoformat(), timeMax=end_time.isoformat()
                                   ).execute()
    return result.get('items', [])


def find_free_slots(events, start_time: datetime, end_time: datetime) -> list[dict[str, datetime]]:
    free_slots = []
    current_time = start_time
    if events:
        for event in events:
            start = datetime.fromisoformat(event['start'].get('dateTime', event['start'].get('date')))
            if start.tzinfo is None:
                start = start.replace(tzinfo=timezone.utc)
            if current_time < start:
                free_slots.append({'start': current_time, 'end': start})
            current_time = datetime.fromisoformat(event['end'].get('dateTime', event['end'].get('date')))
            if current_time.tzinfo is None:
                current_time = current_time.replace(tzinfo=timezone.utc)

    if current_time < end_time:
        free_slots.append({'start': current_time, 'end': end_time})

    return free_slots
