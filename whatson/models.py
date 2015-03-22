from django.db import models
from django.contrib.auth.models import User

class PrivateCalendar(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=32)
    colour = models.CharField(max_length=16)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Private Calendars"

class PrivateEvent(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=32)
    calendar = models.ForeignKey(PrivateCalendar)
    time = models.DateTimeField()
    endTime = models.DateTimeField(default=None)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Private Events"

class PublicCalendar(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    colour = models.CharField(max_length=8)

    def __unicode(self):
        return self.name

    class Meta:
        verbose_name_plural = "Public Calendars"

class PublicEvent(models.Model):
    name = models.CharField(max_length=32)
    calendar = models.ForeignKey(PublicCalendar)
    time = models.DateTimeField()
    endTime = models.DateTimeField(default=None)

    def __unicode(self):
        return self.name

    class Meta:
        verbose_name_plural = "Public Events"

