# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privateevent',
            name='calendar',
        ),
        migrations.DeleteModel(
            name='PrivateEvent',
        ),
        migrations.RemoveField(
            model_name='publicevent',
            name='calendar',
        ),
        migrations.DeleteModel(
            name='PublicCalendar',
        ),
        migrations.DeleteModel(
            name='PublicEvent',
        ),
    ]
