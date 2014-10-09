# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cc_number',
            field=models.IntegerField(max_length=17),
        ),
    ]
