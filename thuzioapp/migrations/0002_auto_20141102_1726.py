# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 2, 17, 26, 29, 52627), blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 2, 17, 26, 29, 53260), blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productpurchase',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 2, 17, 26, 29, 55089), blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 2, 17, 26, 29, 54321), blank=True),
            preserve_default=True,
        ),
    ]
