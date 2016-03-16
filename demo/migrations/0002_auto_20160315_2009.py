# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamereservation',
            old_name='invitaionId',
            new_name='invitationId',
        ),
        migrations.RenameField(
            model_name='gamereservation',
            old_name='promotion',
            new_name='promotionId',
        ),
    ]
