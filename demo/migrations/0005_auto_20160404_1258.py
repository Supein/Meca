# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20160404_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='startTime',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='imagechallenge',
            name='startTime',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='creationDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
