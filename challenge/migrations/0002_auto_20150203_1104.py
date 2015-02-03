# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='time',
        ),
        migrations.AddField(
            model_name='contest',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 3, 11, 4, 42, 609908)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contest',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 3, 11, 4, 42, 609864)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contest',
            name='title',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='content',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='url',
            field=models.CharField(default=b'', max_length=1000),
            preserve_default=True,
        ),
    ]
