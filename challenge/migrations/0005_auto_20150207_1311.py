# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0004_auto_20150203_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('seen', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=300)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 2, 7, 13, 11, 49, 103370))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='contest',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 7, 13, 11, 49, 102596)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contest',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 7, 13, 11, 49, 102546)),
            preserve_default=True,
        ),
    ]
