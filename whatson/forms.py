from django import forms
from django.contrib.auth.models import User
from whatson.models import PrivateCalendar, PrivateEvent
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class NewCalendarForm(forms.ModelForm):

    class Meta:
        model = PrivateCalendar
        fields = ('name', 'colour',)

class NewEventForm(forms.ModelForm):
    time= forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    endTime= forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    class Meta:
        model = PrivateEvent
        fields = ('name', 'calendar', 'time', 'endTime')


