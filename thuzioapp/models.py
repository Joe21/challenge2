from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User)
	address = models.CharField(max_length=80)
	zipcode = models.IntegerField(max_length=5)
	LEVELS = (
		(1, 'Regular'),
		(2, 'Silver'),
		(3, 'Gold'),
		(4, 'Platinum'),
		)
	level = models.IntegerField(max_length=1, choices=LEVELS)
	cc_number = models.IntegerField(max_length=16)

class Purchase(models.Model):
	po_number = models.IntegerField(max_length = 10, unique=True)
	customer = models.ForeignKey(Customer)
	STATUS = (
		(1, 'Processing'),
		(2, 'Shipped'),
		(3, 'Cancelled'),
		(4, 'Backordered'),
		(5, 'Return/Refund'),
		(6, 'Complete')
		)
	status = models.IntegerField(max_length=1, choices=STATUS)
	unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
	shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
	invoice_total = models.DecimalField(max_digits=10, decimal_places=2)

class Product(models.Model):
	purchase = models.ForeignKey(Purchase)
	title = models.CharField(max_length=80)
	description = models.TextField()
	unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
	sell_price = models.DecimalField(max_digits=10, decimal_places=2)
	shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.CharField(max_length=80)
