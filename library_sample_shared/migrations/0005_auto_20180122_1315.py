# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-22 12:15
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_sample_shared', '0004_remove_indexpair_coordinate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpair',
            name='char_coord',
            field=models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[A-Z]$', 'Only capital alpha characters are allowed.')], verbose_name='Character Coordinate'),
        ),
    ]