# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0005_auto_20150320_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('time', models.DateTimeField()),
                ('calendar', models.ForeignKey(to='whatson.PrivateCalendar')),
            ],
            options={
                'verbose_name_plural': 'Private Events',
            },
            bases=(models.Model,),
        ),
    ]
