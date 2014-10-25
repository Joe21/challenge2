# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0004_product_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_address',
            field=models.CharField(max_length=50),
        ),
    ]
