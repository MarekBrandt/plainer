from datetime import datetime, timezone

from app.services.calendar_service import find_free_slots


def test_finds_free_slots_when_one_event():
    one_event = {
        'start': {'dateTime': '2025-01-25T15:00:00+01:00', 'timeZone': 'Europe/Warsaw'},
        'end': {'dateTime': '2025-01-25T15:30:00+01:00', 'timeZone': 'Europe/Warsaw'}, }
    start_time = datetime.fromisoformat('2025-01-24T15:00:00+01:00')
    end_time = datetime.fromisoformat('2025-01-26T15:00:00+01:00')
    slots = find_free_slots([one_event], start_time, end_time)

    assert len(slots) == 2
    assert slots[0]['start'] == start_time
    assert slots[0]['end'] == datetime.fromisoformat(one_event['start']['dateTime'])
    assert slots[1]['start'] == datetime.fromisoformat(one_event['end']['dateTime'])
    assert slots[1]['end'] == end_time


def test_finds_free_slots_when_one_event_with_date_only():
    one_event = {
        'start': {'date': '2025-01-25'},
        'end': {'date': '2025-01-25'}, }
    start_time = datetime.fromisoformat('2025-01-24T15:00:00+01:00')
    end_time = datetime.fromisoformat('2025-01-26T15:00:00+01:00')
    slots = find_free_slots([one_event], start_time, end_time)

    assert len(slots) == 2
    assert slots[0]['start'] == start_time
    assert slots[0]['end'] == datetime.fromisoformat(one_event['start']['date']).replace(tzinfo=timezone.utc)
    assert slots[1]['start'] == datetime.fromisoformat(one_event['end']['date']).replace(tzinfo=timezone.utc)
    assert slots[1]['end'] == end_time
