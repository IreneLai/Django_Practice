# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 05:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0010_auto_20170521_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='date',
        ),
        migrations.RemoveField(
            model_name='image',
            name='uploadDate',
        ),
    ]
