# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20171023_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='client_ID',
        ),
        migrations.RemoveField(
            model_name='user',
            name='client_secret',
        ),
    ]
