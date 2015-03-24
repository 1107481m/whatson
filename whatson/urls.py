from django.conf.urls import patterns, url
from whatson import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^home/', views.home, name='home'),
        url(r'^register/', views.register, name='register'),
        url(r'^login/', views.user_login, name='login'),
        url(r'^logout/', views.user_logout, name='logout'),
        url(r'^about/', views.about, name='about'),
        url(r'^new_calendar/', views.new_calendar, name='new_calendar'),
        url(r'^new_event/', views.new_event, name='new_event'),
        url(r'^get_events/', views.get_events, name='get_events'),
        url(r'^edit_event/', views.edit_event, name='edit_event'),
        url(r'^calendar/', views.calendar, name='calendar'),
        url(r'^export_ical/', views.export_ical, name='export_ical'),
        url(r'^export_googlecal/', views.export_googlecal, name='export_googlecal'),
        url(r'^edit_calendars/', views.edit_calendars, name='edit_calendars'),
        url(r'^import_cal/$', views.import_cal, name='import_cal'),

)