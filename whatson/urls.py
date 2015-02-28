from django.conf.urls import patterns, url
from whatson import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))