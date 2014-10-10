# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0002_auto_20141009_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cost_purchase',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='cost_shipping',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='cost_total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='price_purchase',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='price_shipping',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='price_total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='revenue_total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.IntegerField(max_length=1, null=True, choices=[(1, b'Processing'), (2, b'Shipped'), (3, b'Cancelled'), (4, b'Return/Refund'), (5, b'Complete')]),
        ),
    ]
