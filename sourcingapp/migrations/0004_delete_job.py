# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sourcingapp', '0003_job'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
    ]
