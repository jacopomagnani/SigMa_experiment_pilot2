# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-08 06:53
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0002_auto_20181030_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='num_no',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='num_yes',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='message',
            field=otree.db.models.IntegerField(choices=[[1, 'I agree with the above statement and I pledge to bid 0 in the next rounds.'], [0, 'I do not agree with the above statement and I do not pledge to bid 0 in the next rounds.']], null=True),
        ),
        migrations.AddField(
            model_name='subsession',
            name='part',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='subsession',
            name='round_number_in_part',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
