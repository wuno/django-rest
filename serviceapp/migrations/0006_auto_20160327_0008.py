# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0005_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='commission',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
