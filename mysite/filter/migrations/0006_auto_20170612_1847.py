# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0005_camera_lastmodifieddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='lastModifiedDate',
            field=models.CharField(default='<built-in method now of type object at 0x9dab20>', max_length=100),
        ),
    ]
