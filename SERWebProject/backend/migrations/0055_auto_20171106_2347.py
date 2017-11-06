# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 15:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0054_auto_20171106_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Group')),
                ('team_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_invites', to=settings.AUTH_USER_MODEL)),
                ('teammate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='ddl_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 15, 47, 34, 428760, tzinfo=utc), verbose_name='报名截止日期'),
        ),
        migrations.AlterField(
            model_name='project',
            name='match_data_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 15, 47, 34, 428760, tzinfo=utc), verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 15, 47, 34, 428760, tzinfo=utc), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 6, 15, 47, 34, 428760, tzinfo=utc), verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='clothes_size',
            field=models.CharField(choices=[('XS', 'XS'), ('L', 'L'), ('S', 'S'), ('XL', 'XL'), ('M', 'M')], max_length=2, verbose_name='衣服尺寸'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='backend.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]
