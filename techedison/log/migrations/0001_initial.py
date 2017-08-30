# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContextItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_id', models.CharField(max_length=100)),
                ('org_id', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LogItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('agent', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=100)),
                ('referer', models.CharField(max_length=100)),
                ('accept_language', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('page', models.CharField(max_length=100)),
                ('event_type', models.CharField(max_length=100)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.ContextItems')),
            ],
        ),
    ]