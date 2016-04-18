# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20160315_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('token', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('startTime', models.DateField(default=datetime.datetime(2016, 4, 4, 10, 54, 9, 630774, tzinfo=utc))),
                ('endTime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('solution', models.CharField(max_length=12)),
                ('rawFile', models.ImageField(upload_to='rawImages/')),
            ],
        ),
        migrations.CreateModel(
            name='ImageChallenge',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateField(default=datetime.datetime(2016, 4, 4, 10, 54, 9, 631504, tzinfo=utc))),
                ('endTime', models.DateField()),
                ('image', models.ForeignKey(to='demo.Image')),
                ('parentGame', models.ForeignKey(to='demo.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('token', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('creationDate', models.DateField(default=datetime.datetime(2016, 4, 4, 10, 54, 9, 628191, tzinfo=utc))),
            ],
        ),
        migrations.RemoveField(
            model_name='gamereservation',
            name='tokenId',
        ),
        migrations.AddField(
            model_name='game',
            name='activeChallenge',
            field=models.ForeignKey(to='demo.ImageChallenge', null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='request',
            field=models.ForeignKey(to='demo.GameRequest'),
        ),
        migrations.AddField(
            model_name='game',
            name='reservation',
            field=models.ForeignKey(to='demo.GameReservation'),
        ),
        migrations.AddField(
            model_name='gamereservation',
            name='player',
            field=models.ForeignKey(to='demo.Player', null=True),
        ),
    ]
