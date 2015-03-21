# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0006_privateevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='privateevent',
            name='endTime',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
    ]
