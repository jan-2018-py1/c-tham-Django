# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beltReviewer', '0002_auto_20180224_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1),
        ),
    ]
