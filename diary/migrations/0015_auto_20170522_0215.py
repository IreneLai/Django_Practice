# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 18:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0014_media_diary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='coorX',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='map',
            old_name='coorY',
            new_name='longitude',
        ),
    ]
