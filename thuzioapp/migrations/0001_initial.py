# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_address', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=80)),
                ('zipcode', models.IntegerField(max_length=5)),
                ('cc_number', models.BigIntegerField(max_length=16)),
                ('level', models.IntegerField(max_length=1, choices=[(1, b'Regular'), (2, b'Silver'), (3, b'Gold'), (4, b'Platinum')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_number', models.IntegerField(max_length=10)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('in_stock', models.BooleanField(default=True)),
                ('back_order_till', models.DateField(null=True)),
                ('price_unit_normal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_unit_silver', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_unit_gold', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_unit_platinum', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_shipping', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_shipping_platinum', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('price_total_normal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_total_silver', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_total_gold', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_total_platinum', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_unit', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_shipping', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('po_number', models.IntegerField(max_length=10, unique=True, null=True)),
                ('status', models.IntegerField(default=1, max_length=1, choices=[(1, b'Incomplete'), (2, b'Processing'), (3, b'Shipped'), (4, b'Cancelled'), (5, b'Return/Refund'), (6, b'Complete')])),
                ('price_purchase', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('price_shipping', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('price_total', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('cost_purchase', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('cost_shipping', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('cost_total', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('revenue_total', models.DecimalField(null=True, max_digits=10, decimal_places=2)),
                ('customer', models.ForeignKey(to='thuzioapp.Customer', null=True)),
                ('products', models.ManyToManyField(to='thuzioapp.Product', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
