# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 13:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0065_auto_20171117_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_team_name', models.CharField(default='如：计算机男篮', max_length=20, verbose_name='名称')),
                ('school_team_gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=1, verbose_name='性别')),
                ('school_team_introduction', models.TextField(default='请输入队伍简介(500字以内)', max_length=500, verbose_name='队伍简介')),
                ('school_team_honor', models.TextField(default='请输入队伍成员(500字以内)', max_length=500, verbose_name='队伍成员')),
                ('school_team_image', models.ImageField(upload_to='SchoolTeam')),
                ('school_team_upload_time', models.DateTimeField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 524678, tzinfo=utc), verbose_name='上传时间')),
                ('if_school_team_active', models.BooleanField(default=False, verbose_name='是否激活')),
            ],
            options={
                'verbose_name': '院队 School Team',
                'verbose_name_plural': '院队 School Team',
            },
        ),
        migrations.AlterModelOptions(
            name='carousel',
            options={'verbose_name': '轮播图 Carousel', 'verbose_name_plural': '轮播图 Carousel'},
        ),
        migrations.AlterModelOptions(
            name='halloffame',
            options={'verbose_name': '名人堂 Hall of Fame', 'verbose_name_plural': '名人堂 Hall of Fame'},
        ),
        migrations.AlterField(
            model_name='carousel',
            name='carousel_upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 523675, tzinfo=utc), verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='group',
            name='register_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 521669, tzinfo=utc), verbose_name='报名时间'),
        ),
        migrations.AlterField(
            model_name='halloffame',
            name='HOF_honor',
            field=models.TextField(default='请输入个人荣誉(500字以内)', max_length=500, verbose_name='个人荣誉'),
        ),
        migrations.AlterField(
            model_name='halloffame',
            name='HOF_introduction',
            field=models.TextField(default='请输入个人简介(500字以内)', max_length=500, verbose_name='个人简介'),
        ),
        migrations.AlterField(
            model_name='halloffame',
            name='HOF_upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 524176, tzinfo=utc), verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='register_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 522672, tzinfo=utc), verbose_name='报名时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ddl_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 520165, tzinfo=utc), verbose_name='报名截止日期'),
        ),
        migrations.AlterField(
            model_name='project',
            name='match_data_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 520165, tzinfo=utc), verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 520165, tzinfo=utc), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='projectregisterrelationship',
            name='register_datetime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 521168, tzinfo=utc), verbose_name='报名时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 17, 13, 15, 20, 519163, tzinfo=utc), verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='clothes_size',
            field=models.CharField(choices=[('XS', 'XS'), ('M', 'M'), ('S', 'S'), ('L', 'L'), ('XL', 'XL')], max_length=2, verbose_name='衣服尺寸'),
        ),
    ]
