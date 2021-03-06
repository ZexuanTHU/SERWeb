# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 02:03
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20171101_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRegisterRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_datetime', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='project',
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.TimeField(default=datetime.datetime(2017, 11, 2, 2, 3, 58, 186523, tzinfo=utc), verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='user',
            name='clothes_size',
            field=models.CharField(choices=[('L', 'L'), ('XS', 'XS'), ('M', 'M'), ('XL', 'XL'), ('S', 'S')], max_length=2, verbose_name='衣服尺寸'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='projectregisterrelationship',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='registered_user',
            field=models.ManyToManyField(through='backend.ProjectRegisterRelationship', to=settings.AUTH_USER_MODEL),
        ),
    ]
