# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import filter.models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0012_merge_20170616_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='photo',
            field=models.ImageField(default='static/images/<built-in method now of type object at 0x9dab20>', upload_to=filter.models.renameToPrimaryKey, validators=[filter.models.validateFile]),
        ),
    ]
