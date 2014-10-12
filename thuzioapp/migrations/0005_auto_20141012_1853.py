# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0004_auto_20141012_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='customer',
            field=models.ForeignKey(to='thuzioapp.Customer', null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='po_number',
            field=models.IntegerField(max_length=10, unique=True, null=True),
        ),
    ]
