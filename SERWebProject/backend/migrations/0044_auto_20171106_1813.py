# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 10:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0043_auto_20171106_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectregisterrelationship',
            name='name',
            field=models.CharField(default=None, max_length=20, verbose_name='选手姓名'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ddl_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 10, 13, 24, 995549, tzinfo=utc), verbose_name='报名截止日期'),
        ),
        migrations.AlterField(
            model_name='project',
            name='match_data_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 10, 13, 24, 995549, tzinfo=utc), verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 10, 13, 24, 995549, tzinfo=utc), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 6, 10, 13, 24, 994548, tzinfo=utc), verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='clothes_size',
            field=models.CharField(choices=[('XL', 'XL'), ('S', 'S'), ('L', 'L'), ('M', 'M'), ('XS', 'XS')], max_length=2, verbose_name='衣服尺寸'),
        ),
    ]
