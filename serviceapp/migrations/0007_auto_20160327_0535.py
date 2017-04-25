# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0006_auto_20160327_0008'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advertisers',
            new_name='Advertiser',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='advertiser',
            old_name='advertisers',
            new_name='advertiser',
        ),
    ]
