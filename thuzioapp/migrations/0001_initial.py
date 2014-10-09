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
                ('cc_number', models.IntegerField(max_length=16)),
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
                ('image', models.CharField(max_length=80)),
                ('in_stock', models.BooleanField(default=True)),
                ('back_order_till', models.DateField()),
                ('price_unit', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_shipping', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_unit', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_shipping', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('po_number', models.IntegerField(unique=True, max_length=10)),
                ('status', models.IntegerField(max_length=1, choices=[(1, b'Processing'), (2, b'Shipped'), (3, b'Cancelled'), (4, b'Return/Refund'), (5, b'Complete')])),
                ('price_purchase', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_shipping', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_purchase', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_shipping', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cost_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('revenue_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('customer', models.ForeignKey(to='thuzioapp.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase',
            field=models.ForeignKey(to='thuzioapp.Purchase'),
            preserve_default=True,
        ),
    ]
