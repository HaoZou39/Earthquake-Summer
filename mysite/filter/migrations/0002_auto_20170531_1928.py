# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip_camera',
            name='camera_id',
        ),
        migrations.RemoveField(
            model_name='non_ip_camera',
            name='camera_id',
        ),
        migrations.AlterField(
            model_name='camera',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ip_camera_model',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]