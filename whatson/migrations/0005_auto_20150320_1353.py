# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0004_auto_20150318_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatecalendar',
            name='colour',
            field=models.CharField(max_length=16),
        ),
    ]
