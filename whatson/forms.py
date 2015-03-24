from django import forms
from django.contrib.auth.models import User
from whatson.models import PrivateCalendar, PrivateEvent
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

#Register form
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
    # Date time widgets to add automatic dropdown JS select menu
    time= forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    endTime= forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    def __init__(self, request, *args, **kwargs):
        # request is a required parameter for this form.
        super(NewEventForm, self).__init__(*args, **kwargs)
        self.fields['calendar'].queryset = PrivateCalendar.objects.filter(user=request.user)

    class Meta:
        model = PrivateEvent
        fields = ('name', 'calendar', 'time', 'endTime')

class EditEventForm(forms.ModelForm):
    # Date time widgets to add automatic dropdown JS select menu
    time= forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    endTime= forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    class Meta:
        model = PrivateEvent
        fields = ('name', 'calendar', 'time', 'endTime')

class EditCalendarsForm(forms.ModelForm):
    active = forms.BooleanField()
    name = forms.CharField(initial="da")
    class Meta:
        model = PrivateCalendar
        fields = ('name', 'active')


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Please select a file in .ics or .csv format'
    )