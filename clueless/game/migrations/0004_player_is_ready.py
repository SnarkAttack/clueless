# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_player_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
