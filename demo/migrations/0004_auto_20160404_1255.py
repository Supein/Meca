# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20160404_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='startTime',
            field=models.DateField(default=datetime.datetime(2016, 4, 4, 10, 55, 2, 612772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='imagechallenge',
            name='startTime',
            field=models.DateField(default=datetime.datetime(2016, 4, 4, 10, 55, 2, 613619, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='player',
            name='creationDate',
            field=models.DateField(default=datetime.datetime(2016, 4, 4, 10, 55, 2, 609435, tzinfo=utc)),
        ),
    ]
