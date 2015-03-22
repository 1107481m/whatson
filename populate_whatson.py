import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatson_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from whatson.models import PrivateCalendar, PrivateEvent, PublicCalendar, PublicEvent


def populate():
    # Create user test
    add_user(username="test", password="test")

    # Add 3 events to user 1 (test account) calendars
    add_private_calendar(1, "test calendar 1", "#FEFEFE")
    add_private_calendar(1, "test calendar 2", "#000000")
    add_private_calendar(1, "test calendar 3", "#666666")

    # Add events to test users calendars
    add_private_event("test event 1", 1, "2015-03-2 19:00", "2015-03-22 19:00", 1)
    add_private_event("test event 2", 2, "2015-03-22 03:00", "2015-03-27 01:00", 1)
    add_private_event("test event 3", 2, "2015-03-30 15:00", "2015-04-01 19:00", 1)
    add_private_event("test event 4", 2, "2015-03-05 12:00", "2015-03-06 09:21", 1)
    add_private_event("test event 5", 3, "2015-03-06 13:30", "2015-03-07 03:00", 1)
    add_private_event("test event 6", 3, "2015-03-01 19:40", "2015-03-01 19:00", 1)

    # Create public calendars
    add_public_calendar("test calendar 1", "this is the description for test calendar 1", "#FFFFFF")
    add_public_calendar("test calendar 2", "this is the description for test calendar 2", "#888888")
    add_public_calendar("test calendar 3", "this is the description for test calendar 3", "#000000")
    add_public_calendar("test calendar 4", "this is the description for test calendar 4", "#FEFEFE")

    # Create public events
    add_public_event("test event 1", 1, "2015-03-01 19:00", "2015-03-22 19:00")
    add_public_event("test event 2", 2, "2015-03-21 03:00", "2015-03-27 01:00")
    add_public_event("test event 3", 2, "2015-03-29 15:00", "2015-04-01 19:00")
    add_public_event("test event 4", 2, "2015-03-03 12:00", "2015-03-06 09:21")
    add_public_event("test event 5", 3, "2015-03-03 13:30", "2015-03-07 03:00")
    add_public_event("test event 6", 3, "2015-02-22 19:40", "2015-03-01 19:00")

def add_private_calendar(user, name, colour):
    pc = PrivateCalendar.objects.get_or_create(user_id=user, name=name, colour=colour)
    return pc

def add_private_event(name, calendar, time, endTime, user):
    pe = PrivateEvent.objects.get_or_create(name=name, calendar_id=calendar, time=time, endTime=endTime, user_id=user)
    return pe

def add_public_calendar(name, description, colour):
    pc = PublicCalendar.objects.get_or_create(name=name, description=description, colour=colour)
    return pc

def add_public_event(name, calendar, time, endTime):
    pe = PublicEvent.objects.get_or_create(name=name, calendar_id=calendar, time=time, endTime=endTime)
    return pe

def add_user(username, password):
    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.save()
    return user

# Start execution here!
if __name__ == '__main__':
    print "Starting WhatsOn population script..."
    populate()
    print "Populate script execution ended"


