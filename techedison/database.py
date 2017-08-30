import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techedison.settings")
django.setup()

import click
import openpyxl
import MySQLdb

import psycopg2
from django.core.management import execute_from_command_line
from log import models
from techedison import settings
db=settings.DATABASES['default']
dbname=db['NAME']
dbuser=db['USER']
dbpass=db['PASSWORD']



import json
import codecs
data = []
context_item=[]
i=0
with codecs.open('Tracking-Log.txt','rU','utf-8') as f:
    for line in f:
       data.append(json.loads(line))
       x = data[i]
       context_item.append(x["context"])
       i += 1


@click.group()
def cli():
    pass
@click.command()
def createDb():
    db1 = psycopg2.connect(host="localhost", user=dbuser, passwd=dbpass)
    cursor = db1.cursor()
    sql = """CREATE DATABASE %s""" % dbname
    cursor.execute(sql)
    args = ["manage.py", "flush", "--no-input"]
    execute_from_command_line(args)
    args = ["manage.py", "makemigrations"]
    execute_from_command_line(args)
    args = ["manage.py", "migrate"]
    execute_from_command_line(args)
    db1.commit()

cli.add_command(createDb)

@click.command()
def dummy():
    n=0
    for i in range(0, len(context_item), 1):
        col = models.ContextItems()
        serial_id = n
        n+=1
        col.course_id = str(context_item[i]["course_id"])
        col.org_id = str(context_item[i]["org_id"])
        col.path = str(context_item[i]["path"])
        col.user_id = str(context_item[i]["user_id"])
        col.save()


    n=0
    for i in range(0, len(data), 1):
        c = n
        n+=1
        col=models.LogItems()
        col.username=str(data[i]["username"])
        col.context=c
        #col.name=str(data[i]["name"])
        col.ip=str(data[i]["ip"])
        col.agent=str(data[i]["agent"])
        #col.event=str(data[i]["event"])
        col.host=str(data[i]["host"])
        #col.session=str(data[i]["session"])
        col.referer=str(data[i]["referer"])
        col.accept_language=str(data[i]["accept_language"])
        col.time=str(data[i]["time"])
        col.page=str(data[i]["page"])
        col.event_type=str(data[i]["event_type"])
        col.save()
cli.add_command(dummy)

@click.command()
def cleardb():
    db1 = MySQLdb.connect(host="localhost", user=dbuser, passwd=dbpass)
    args = ["manage.py", "flush", "--no-input"]
    execute_from_command_line(args)
    db1.commit()
cli.add_command(cleardb)
if __name__=='__main__':
    cli()