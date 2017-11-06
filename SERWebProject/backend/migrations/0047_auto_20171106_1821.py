# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 10:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0046_auto_20171106_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ddl_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 10, 21, 56, 841989, tzinfo=utc), verbose_name='报名截止日期'),
        ),
        migrations.AlterField(
            model_name='project',
            name='match_data_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 10, 21, 56, 841989, tzinfo=utc), verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 10, 21, 56, 841989, tzinfo=utc), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='projectregisterrelationship',
            name='name',
            field=models.CharField(default='选手', max_length=10, verbose_name='选手姓名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 6, 10, 21, 56, 840993, tzinfo=utc), verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='clothes_size',
            field=models.CharField(choices=[('XL', 'XL'), ('L', 'L'), ('XS', 'XS'), ('S', 'S'), ('M', 'M')], max_length=2, verbose_name='衣服尺寸'),
        ),
    ]
