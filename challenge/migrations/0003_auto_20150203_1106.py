# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_auto_20150203_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='code',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 3, 11, 6, 33, 26596)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 3, 11, 6, 33, 26541)),
            preserve_default=True,
        ),
    ]
