# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0012_auto_20170829_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contextitems',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]