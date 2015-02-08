# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_auto_20150208_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 8, 5, 39, 677395)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 8, 5, 39, 677348)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 8, 5, 39, 678214)),
            preserve_default=True,
        ),
    ]
