from django.db import models
from django.contrib.auth.models import User



class PrivateCalendar(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    colour = models.CharField(max_length=8)

    def __unicode(self):
        return self.name

    class Meta:
        verbose_name_plural = "Private Calendars"

class PrivateEvent(models.Model):
    name = models.CharField(max_length=32)
    calendar = models.ForeignKey(PrivateCalendar)
    time = models.DateTimeField()
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Private Events"

class PublicCalendar(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    colour = models.CharField(max_length=8)
    time = models.DateTimeField()
    def __unicode(self):
        return self.name

    class Meta:
        verbose_name_plural = "Public Calendars"

class PublicEvent(models.Model):
    name = models.CharField(max_length=32)
    calendar = models.ForeignKey(PublicCalendar)

    def __unicode(self):
        return self.name

    class Meta:
        verbose_name_plural = "Public Events"

