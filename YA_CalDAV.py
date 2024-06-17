import datetime
import caldav
import os

def push_caldav(start, end, sum):
    with caldav.DAVClient(url=os.environ['CALDAV_URL'], 
			username=os.environ['USERNAME'], 
			password=os.environ['PASSWORD']) as client:
        my_principal = client.principal()
        calendar = my_principal.calendar('test')
        calendar.save_event(
            dtstart=start,
            dtend=end,
            summary=sum,
        )



# with caldav.DAVClient(url=CALDAV_URL, username=USERNAME, password=PASSWORD) as client:
#     my_principal = client.principal()
#     calendar = my_principal.calendar('test')
#     print(calendar.date_search(datetime.datetime.now())[0].data)

'''
BEGIN: VEVENT
DTSTART
TZID = Europe/Moscow: 20240617T133000
DTEND
TZID = Europe/Moscow: 20240617T134500
SUMMARY: Название
UID: 1p3bn2do462ctrjmcayandex.ru
SEQUENCE: 0
DTSTAMP: 20240617T103620Z
CREATED: 20240617T103153Z
LOCATION: 111
DESCRIPTION: описание
URL: https: // calendar.yandex.ru/event?event_id = 2119684346
TRANSP: OPAQUE
CATEGORIES: test
ORGANIZER
CN = "Бабушкин Александр": mailto: e0m.ru@yandex.ru
ATTENDEE
PARTSTAT = NEEDS-ACTION
CN = i
ROLE = REQ-PARTICIPANT: mailto: i@e0m.ru
ATTENDEE
PARTSTAT = ACCEPTED
CN = "Бабушкин Александр"
ROLE = REQ-PARTICIPANT: mailto: e0m.ru@yandex.ru
ATTENDEE
PARTSTAT = NEEDS-ACTION
CN = ctspi
ROLE = OPT-PARTICIPANT: mailto: ctspi@ctspi.ru
LAST-MODIFIED: 20240617T103153Z
CLASS: PRIVATE
END: VEVENT
END: VCALENDAR
'''
