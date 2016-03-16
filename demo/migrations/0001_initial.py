# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('validationId', models.CharField(max_length=10)),
                ('invitaionId', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GameReservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('tokenId', models.CharField(max_length=10)),
                ('invitaionId', models.CharField(max_length=10)),
                ('promotion', models.BooleanField(default=True)),
            ],
        ),
    ]
