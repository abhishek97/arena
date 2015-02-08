# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_auto_20150207_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 7, 41, 48, 327172)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 7, 41, 48, 327125)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 7, 41, 48, 327987)),
            preserve_default=True,
        ),
    ]
