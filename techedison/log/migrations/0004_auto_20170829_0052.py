# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20170829_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logitems',
            name='accept_language',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='agent',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='event',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='event_type',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='host',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='ip',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='page',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='referer',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='session',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='time',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='username',
            field=models.CharField(max_length=500),
        ),
    ]
