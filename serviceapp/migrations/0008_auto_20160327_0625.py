# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0007_auto_20160327_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertiser',
            old_name='advertiser',
            new_name='singleAdvertiser',
        ),
    ]
