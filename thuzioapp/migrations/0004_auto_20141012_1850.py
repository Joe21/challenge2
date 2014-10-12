# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0003_auto_20141009_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.IntegerField(max_length=1, null=True, choices=[(1, b'Incomplete'), (2, b'Processing'), (3, b'Shipped'), (4, b'Cancelled'), (5, b'Return/Refund'), (6, b'Complete')]),
        ),
    ]
