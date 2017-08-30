# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0009_auto_20170829_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contextitems',
            name='course_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contextitems',
            name='org_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contextitems',
            name='path',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contextitems',
            name='user_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='logitems',
            name='username',
            field=models.TextField(),
        ),
    ]
