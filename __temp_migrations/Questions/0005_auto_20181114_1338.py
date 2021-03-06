# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-14 09:38
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0004_auto_20181112_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='q2',
            field=otree.db.models.IntegerField(choices=[[1, 'Player B will earn 7 points.'], [2, 'Player B will earn either 7 points or 1 point.'], [3, 'Player B may earn any of the following amounts of points: 7, 1 or -3.']], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='q3',
            field=otree.db.models.IntegerField(choices=[[1, 'Player B will earn 12 points.'], [2, 'Player B will earn either 12 points or 4 points.'], [3, 'Player B may earn any of the following amounts of points: 12, 4 or -8.']], null=True),
        ),
    ]
