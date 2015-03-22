from django.contrib import admin
from whatson.models import PrivateCalendar, PrivateEvent, PublicCalendar, PublicEvent


admin.site.register(PrivateCalendar)
admin.site.register(PrivateEvent)
admin.site.register(PublicCalendar)
admin.site.register(PublicEvent)


class PrivateCalendarAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'colour')

class PrivateEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'calendar', 'time')