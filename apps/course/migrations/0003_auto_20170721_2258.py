# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20170721_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]