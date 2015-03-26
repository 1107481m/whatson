from django.test import TestCase, Client
from whatson.models import PrivateCalendar,PrivateEvent,PublicCalendar,PublicEvent
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth import models
from django.contrib.auth.models import User

class PrivateCalendarModelTests(TestCase):

    def test_PrivateCalendar__unicode___is_name_of_calendar(self):
        """
            PrivateCalendar__unicode__is_name_of_calendar should return true if __unicode__ matches correct name of calendar
        """
        calendarName = "test"
        cal = PrivateCalendar(name=calendarName,colour=0000,active=True)

        self.assertEqual((cal.__unicode__() == calendarName), True)

    def test_PrivateEvent_belongs_to_PrivateCalendar(self):
        """
        PrivateEvent_belongs_to_PrivateCalendar returns true if PrivateEvent can be correctly associated with PrivateCalendar
        """
        cal = PrivateCalendar(name="Test Calender",colour=0000,active=True)
        event = PrivateEvent(name="Test Event", calendar=cal, time=datetime.now,endTime=datetime.now)
        self.assertEqual((event.calendar.name == cal.name), True)

class PublicCalendarModelTests(TestCase):

    def test_PublicCalendar__unicode___is_name_of_calendar(self):
        """
            PublicCalendar__unicode__is_name_of_calendar should return true if __unicode__ matches correct name of calendar
        """
        calendarName = "test"
        cal = PublicCalendar(name=calendarName,colour=0000)

        self.assertEqual((cal.__unicode__() == calendarName), True)

    def test_PublicEvent_belongs_to_PublicCalendar(self):
        """
        PublicEvent_belongs_to_PublicCalendar returns true if PublicEvent can be correctly associated with PublicCalendar
        """
        cal = PublicCalendar(name="Test Calender",colour=0000)
        event = PublicEvent(name="Test Event", calendar=cal, time=datetime.now,endTime=datetime.now)
        self.assertEqual((event.calendar.name == cal.name), True)

class HomeViewTests(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('Ross', 'ross@ross.com', 'password')

    def login(self):
        self.c.login(username='Ross', password='password')

    def test_only_logged_in_users_can_view_home(self):
        """
        only_logged_in_users_can_view_home tests that a redirect status code occurs when going to /home/ without loggin in
        also tests that a logged in user can go to /home/ without being directed (status.code = 200)
        """
        response = self.c.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

        self.login()
        response = self.c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_welcomes_correct_username(self):
        """
        home_welcomes_correct_username tests homepage recognises user and uses the correct username in its welcome message
        """
        self.login()
        response = self.c.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Welcome back, Ross!')
