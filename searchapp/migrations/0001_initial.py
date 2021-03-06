# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=500)),
                ('job_description', models.TextField(max_length=10000)),
                ('job_status', models.CharField(max_length=500)),
                ('skill_set', models.CharField(max_length=500)),
                ('keywords', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
