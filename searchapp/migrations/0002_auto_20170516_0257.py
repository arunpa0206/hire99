# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='amazon', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='job_location',
            field=models.CharField(default='Bangalore', max_length=500),
            preserve_default=False,
        ),
    ]
