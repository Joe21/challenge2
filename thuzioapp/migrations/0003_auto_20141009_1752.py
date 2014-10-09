# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0002_auto_20141009_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cc_number',
            field=models.BigIntegerField(max_length=16),
        ),
    ]
