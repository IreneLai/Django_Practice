# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 07:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0012_auto_20170521_1336'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Media',
        ),
        migrations.DeleteModel(
            name='Vedio',
        ),
    ]