# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 09:32
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'initial_data', app_label='library')


def unload_fixture(apps, schema_editor):
    LibraryProtocol = apps.get_model('library', 'LibraryProtocol')
    LibraryType = apps.get_model('library', 'LibraryType')
    LibraryType.objects.all().delete()
    LibraryProtocol.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture)
    ]