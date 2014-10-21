# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0003_auto_20141019_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
