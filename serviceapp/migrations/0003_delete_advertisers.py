# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 03:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0002_auto_20160326_0229'),
    ]

    operations = [
        migrations.DeleteModel(
            name='advertisers',
        ),
    ]