# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagassist', '0008_auto_20171005_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='sympNumber',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
