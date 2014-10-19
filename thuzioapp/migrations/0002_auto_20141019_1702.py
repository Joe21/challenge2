# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='bill_to_address',
            field=models.CharField(max_length=80, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='bill_to_cc_number',
            field=models.BigIntegerField(max_length=16, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='bill_to_zipcode',
            field=models.IntegerField(max_length=5, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='ship_to_address',
            field=models.CharField(max_length=80, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='ship_to_zipcode',
            field=models.IntegerField(max_length=5, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cc_number',
            field=models.BigIntegerField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(max_length=5, null=True),
        ),
    ]
