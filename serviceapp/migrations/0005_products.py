# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0004_advertisers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('product_id', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_url', models.CharField(max_length=100)),
                ('advertiser', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=100)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('commission', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
    ]
