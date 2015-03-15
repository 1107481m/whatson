# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('colour', models.CharField(max_length=8)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Private Calendars',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrivateEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('calendar', models.ForeignKey(to='whatson.PrivateCalendar')),
            ],
            options={
                'verbose_name_plural': 'Private Events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('colour', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Public Calendars',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('calendar', models.ForeignKey(to='whatson.PublicCalendar')),
            ],
            options={
                'verbose_name_plural': 'Public Events',
            },
            bases=(models.Model,),
        ),
    ]
