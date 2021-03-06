# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(choices=[('MAYOR-ROAD', 'Mayor-Road'), ('RONGAI', 'rongai'), ('GATAKA', 'gataka'), ('OLOLUA', 'ololua')], max_length=60)),
                ('occupants_count', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dept', models.CharField(blank=True, max_length=50, null=True)),
                ('institution_category', models.CharField(choices=[('PUBLIC', 'public'), ('PRIVATE', 'private')], max_length=60)),
                ('outstanding', models.CharField(choices=[('COMMUNISM', 'Communism'), ('EXCELLENCE', 'Excellence'), ('COMPASION', 'Compasion'), ('INTEGRITY', 'Integrity')], max_length=60)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood_app.Hood')),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dept', models.CharField(blank=True, max_length=50, null=True)),
                ('institution_category', models.CharField(choices=[('RACISM', 'racism'), ('BAD-SERVICES', 'Bad-Services'), ('BRIBERY', 'Bribery')], max_length=60)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood_app.Hood')),
            ],
        ),
    ]
