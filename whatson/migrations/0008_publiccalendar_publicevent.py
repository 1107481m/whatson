# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0007_privateevent_endtime'),
    ]

    operations = [
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
                ('time', models.DateTimeField()),
                ('endTime', models.DateTimeField(default=None)),
                ('calendar', models.ForeignKey(to='whatson.PublicCalendar')),
            ],
            options={
                'verbose_name_plural': 'Public Events',
            },
            bases=(models.Model,),
        ),
    ]
