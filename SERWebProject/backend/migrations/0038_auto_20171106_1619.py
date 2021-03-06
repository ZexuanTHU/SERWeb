# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 08:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0037_auto_20171106_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectregisterrelationship',
            name='if_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='ddl_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 8, 19, 13, 274837, tzinfo=utc), verbose_name='报名截止日期'),
        ),
        migrations.AlterField(
            model_name='project',
            name='match_data_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 8, 19, 13, 274837, tzinfo=utc), verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 8, 19, 13, 274837, tzinfo=utc), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 6, 8, 19, 13, 274837, tzinfo=utc), verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='clothes_size',
            field=models.CharField(choices=[('L', 'L'), ('XL', 'XL'), ('XS', 'XS'), ('M', 'M'), ('S', 'S')], max_length=2, verbose_name='衣服尺寸'),
        ),
    ]
