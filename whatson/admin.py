from django.contrib import admin
from whatson.models import PrivateCalendar#, PrivateEvent, PublicCalendar, PublicEvent





# Register your models here.
admin.site.register(PrivateCalendar)
'''
admin.site.register(PrivateEvent)
admin.site.register(PublicCalendar)
admin.site.register(PublicEvent)
'''

class PrivateCalendarAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'colour')