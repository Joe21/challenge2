# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thuzioapp', '0002_auto_20141019_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_300x200',
            field=models.CharField(default=b'http://prairieceramics.com/wpress/here/wp-content/uploads/2013/10/cache/image_coming_soon-300x200.jpg', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='image_600x400',
            field=models.CharField(default=b'http://placekitten.com/g/600/400', max_length=200),
            preserve_default=True,
        ),
    ]
