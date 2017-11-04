# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 16:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_auto_20171105_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_login',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 4, 16, 41, 21, 409596, tzinfo=utc), verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='clothes_size',
            field=models.CharField(choices=[('M', 'M'), ('XL', 'XL'), ('S', 'S'), ('XS', 'XS'), ('L', 'L')], max_length=2, verbose_name='衣服尺寸'),
        ),
    ]
