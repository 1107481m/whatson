from django import forms
from django.contrib.auth.models import User
from whatson.models import PrivateCalendar
from whatson.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class NewCalendarForm(forms.ModelForm):

    class Meta:
        model = PrivateCalendar
        fields = ('name', 'colour',)
