# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worefApp', '0003_auto_20171029_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kunden',
            name='BLZ',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='kunden',
            name='Telefon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
