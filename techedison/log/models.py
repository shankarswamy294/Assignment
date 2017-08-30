# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ContextItems(models.Model):
    serial_id=models.IntegerField(primary_key=True,default=1)
    course_id = models.TextField(default='-1')
    org_id = models.TextField(default='-1')
    path = models.TextField(default='-1')
    user_id = models.CharField(max_length=10,default='-1')

    def __unicode__(self):
        return unicode(self.serial_id)

class LogItems(models.Model):
    username=models.TextField()
    #context=models.ForeignKey(ContextItems)
    name=models.CharField(max_length=200,)
    ip=models.CharField(max_length=200,default='-1')
    agent=models.CharField(max_length=200,default='-1')
    #event=models.TextField(max_length=500,default='-1')
    host=models.CharField(max_length=200,default='-1')
    #session=models.CharField(max_length=200,default='-1')
    referer=models.CharField(max_length=200,default='-1')
    accept_language=models.CharField(max_length=200,default='-1')
    time=models.CharField(max_length=200,default='-1')
    page=models.CharField(max_length=200,default='-1')
    event_type=models.CharField(max_length=200,default='-1')

    def __unicode__(self):
        return unicode(self.username)