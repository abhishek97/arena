# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_auto_20150203_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='code',
            field=models.CharField(default=b'A unique code here', unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 3, 15, 28, 24, 859860)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 3, 15, 28, 24, 859809)),
            preserve_default=True,
        ),
    ]
