# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagassist', '0007_auto_20171005_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostic',
            name='ICD10',
            field=models.CharField(max_length=10),
        ),
    ]