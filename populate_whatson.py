import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatson_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from whatson.models import PrivateCalendar, PrivateEvent, PublicCalendar, PublicEvent


def populate():
    # Create user test
    add_user(username="test", password="test") #Leif's logon for assessment
    add_user(username="John", password="password")
    add_user(username="Susie", password="password")
    ###########################################################

    # Add 3 calendars to test
    add_private_calendar(1, "test calendar 1", "#FEFEFE")
    add_private_calendar(1, "test calendar 2", "#000000")
    add_private_calendar(1, "test calendar 3", "#666666")
	
    # Add 3 calendars to John
    add_private_calendar(2, "University timetable", "#FF0000")
    add_private_calendar(2, "Football & gigs", "#000000")
	
    # Add 3 calendars to Susie
    add_private_calendar(3, "Work meetings", "#FEFEFE")
    add_private_calendar(3, "Jack' calendar", "#000000")
    add_private_calendar(3, "Rachael's calendar", "#FF0000")
    ############################################################

    # Add events to test users calendars
    add_private_event("test event 1", 1, "2015-03-2 19:00", "2015-03-22 19:00", 1)
    add_private_event("test event 2", 2, "2015-03-22 03:00", "2015-03-27 01:00", 1)
    add_private_event("test event 3", 2, "2015-03-30 15:00", "2015-04-01 19:00", 1)
    add_private_event("test event 4", 2, "2015-03-05 12:00", "2015-03-06 09:21", 1)
    add_private_event("test event 5", 3, "2015-03-06 13:30", "2015-03-07 03:00", 1)
    add_private_event("test event 6", 3, "2015-03-01 19:40", "2015-03-01 19:00", 1)
	
    # Add events to John's calendars
    add_private_event("JOOSE 2 (Lecture)", 1, "2015-03-02 11:00", "2015-03-02 12:00", 2)
    add_private_event("ADS2 (Lecture)", 1, "2015-03-03 11:00", "2015-03-03 12:00", 2)
    add_private_event("Web App Development (Lecture)", 1, "2015-03-04 11:00", "2015-04-04 12:00", 2)
    add_private_event("JOOSE 2 (Lecture)", 1, "2015-03-04 13:00", "2015-03-04 14:00", 2)
    add_private_event("Web App Development (Lab)", 1, "2015-03-04 14:00", "2015-03-04 16:00", 2)
    add_private_event("ADS2 (Lecture)", 1, "2015-03-05 11:00", "2015-03-05 12:00", 2)
    add_private_event("Web App Development (Lecture)", 1, "2015-03-06 11:00", "2015-03-01 12:00", 2)
    add_private_event("ADS2 (Examples)", 1, "2015-03-06 13:00", "2015-03-06 14:00", 2)
    add_private_event("JOOSE 2 (Tutorial)", 1, "2015-03-01 14:00", "2015-03-01 15:00", 2)
    add_private_event("Hearts vs Motherwell", 2, "2015-03-01 19:00", "2015-03-01 21:00", 2)
    ############### Week 2 (March)
    add_private_event("JOOSE 2 (Lecture)", 1, "2015-03-09 11:00", "2015-03-09 12:00", 2)
    add_private_event("ADS2 (Lecture)", 1, "2015-03-10 11:00", "2015-03-10 12:00", 2)
    add_private_event("Web App Development (Lecture)", 1, "2015-03-11 11:00", "2015-04-11 12:00", 2)
    add_private_event("JOOSE 2 (Lecture)", 1, "2015-03-04 13:00", "2015-03-04 14:00", 2)
    add_private_event("Web App Development (Lab)", 1, "2015-03-04 14:00", "2015-03-04 16:00", 2)
    add_private_event("ADS2 (Lecture)", 1, "2015-03-05 11:00", "2015-03-05 12:00", 2)
    add_private_event("Web App Development (Lecture)", 1, "2015-03-06 11:00", "2015-03-01 12:00", 2)
    add_private_event("ADS2 (Examples)", 1, "2015-03-06 13:00", "2015-03-06 14:00", 2)
    add_private_event("JOOSE 2 (Tutorial)", 1, "2015-03-01 14:00", "2015-03-01 15:00", 2)
    add_private_event("Hearts vs Celtic", 2, "2015-03-01 19:00", "2015-03-01 21:00", 2)
    ############### Week 3 (March)
    add_private_event("JOOSE 2 (Lecture)", 1, "2015-03-09 11:00", "2015-03-09 12:00", 2)
    add_private_event("ADS2 (Lecture)", 1, "2015-03-10 11:00", "2015-03-10 12:00", 2)
    add_private_event("Web App Development (Lecture)", 1, "2015-03-11 11:00", "2015-04-11 12:00", 2)
    add_private_event("JOOSE 2 (Lecture)", 1, "2015-03-04 13:00", "2015-03-04 14:00", 2)
    add_private_event("Web App Development (Lab)", 1, "2015-03-04 14:00", "2015-03-04 16:00", 2)
    add_private_event("ADS2 (Lecture)", 1, "2015-03-05 11:00", "2015-03-05 12:00", 2)
    add_private_event("Web App Development (Lecture)", 1, "2015-03-06 11:00", "2015-03-01 12:00", 2)
    add_private_event("ADS2 (Examples)", 1, "2015-03-06 13:00", "2015-03-06 14:00", 2)
    add_private_event("JOOSE 2 (Tutorial)", 1, "2015-03-01 14:00", "2015-03-01 15:00", 2)
    add_private_event("Hearts vs Rangers", 2, "2015-03-01 19:00", "2015-03-01 21:00", 2)
	
    # Add events to Susie's calendars
    add_private_event("Client meeting", 1, "2015-03-02 13:10", "2015-03-02 13:40", 3)
    add_private_event("Shipping meeting", 2, "2015-03-02 14:00", "2015-03-02 15:00", 3)
    add_private_event("HR Meeting", 2, "2015-03-03 10:00", "2015-04-03 11:30", 3)
    add_private_event("test event 4", 2, "2015-03-05 12:00", "2015-03-06 09:21", 3)
    add_private_event("test event 5", 3, "2015-03-06 13:30", "2015-03-07 03:00", 3)
    add_private_event("test event 6", 3, "2015-03-01 19:40", "2015-03-01 19:00", 3)

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


