# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_auto_20170829_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contextitems',
            name='course_id',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contextitems',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contextitems',
            name='org_id',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='username',
            field=models.TextField(max_length=20),
        ),
    ]
