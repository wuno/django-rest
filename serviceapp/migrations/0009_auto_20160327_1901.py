# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0008_auto_20160327_0625'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Advertiser',
        ),
        migrations.AlterField(
            model_name='product',
            name='advertiser',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='commission',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='designer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_url',
            field=models.CharField(max_length=255),
        ),
    ]
