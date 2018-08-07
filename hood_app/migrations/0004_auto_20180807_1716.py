# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 14:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood_app', '0003_auto_20180807_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='reports',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]