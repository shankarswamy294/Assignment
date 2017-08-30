# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.views import generic,View
from django.views.generic.edit import CreateView
from .models import ContextItems,LogItems
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader
import json

# Create your views here.


def fullList(request):
    result= LogItems.objects.all()
    y=[]
    for i in result:
        if i.username=="":
            y.append("annonamus")
        else:
            y.append(i.username)
    z=set(y)

    video_played = []
    enrolled=[]
    for j in z:
        c=0
        k=0
        for i in result:
            if i.username == j:
                if i.event_type == "play_video":
                    c+=1
                if i.event_type == "te.course.enrollment.activated":
                    k+=1
        video_played.append(c)
        enrolled.append(k)

    final=[]
    z=list(z)
    for i in range(0,len(z),1):
        new=[]
        new.append(z[i])
        new.append(video_played[i])
        new.append(enrolled[i])
        final.append(new)
        print z

    arr = [str(r) for r in list(z)]
    #result1= TodoItem.objects.filter(name__name = name)

    template = loader.get_template('log/index.html')
    context = {
        'arr': arr,
        'video_played': video_played,
        'enrolled':enrolled,
        "final":final
    }
    return HttpResponse(template.render(context, request))
