# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 07:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_filed',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
