from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
	# Establish link btwn User model and Customer
	user = models.OneToOneField(User)

	# Fields for Customer Model
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email_address = models.CharField(max_length=20)
	address = models.CharField(max_length=80)
	zipcode = models.IntegerField(max_length=5)
	cc_number = models.BigIntegerField(max_length=16)

	###	Choice field for customer discount level	 
	LEVELS = (
		(1, 'Regular'),
		(2, 'Silver'),
		(3, 'Gold'),
		(4, 'Platinum'),
		)
	level = models.IntegerField(max_length=1, choices=LEVELS)

	def __unicode__(self):
		return self.first_name


class Purchase(models.Model):
	# Establish link btwn Purchase model and Customer model
	customer = models.ForeignKey(Customer)

	# Fields for Purchase model
	###	Purchase Order number must remain unique
	po_number = models.IntegerField(max_length = 10, unique=True)

	### Choice field for purchase status
	STATUS = (
		(1, 'Processing'),
		(2, 'Shipped'),
		(3, 'Cancelled'),
		(4, 'Return/Refund'),
		(5, 'Complete')
		)
	status = models.IntegerField(max_length=1, choices=STATUS)

	### Total price of purchase to customer
	price_purchase = models.DecimalField(max_digits=10, decimal_places=2)

	### Shipping price of purchase to customer
	price_shipping = models.DecimalField(max_digits=10, decimal_places=2)

	### Total price on invoice to customer
	price_total = models.DecimalField(max_digits=10, decimal_places=2)
	
	### Total cost of purchase to Thuzio
	cost_purchase = models.DecimalField(max_digits=10, decimal_places=2)

	### Shipping cost of purchase to Thuzio
	cost_shipping = models.DecimalField(max_digits=10, decimal_places=2)

	### Total cost of purchase to Thuzio
	cost_total = models.DecimalField(max_digits=10, decimal_places=2)

	### Total revenue of purchase to Thuzio
	revenue_total = models.DecimalField(max_digits=10, decimal_places=2)

	def unicode(self):
		return "PO# {}".format(self.po_number)


class Product(models.Model):
	# Establish link btwn Product model and Purchase model
	purchase = models.ForeignKey(Purchase)

	# Fields for Product model
	model_number = models.IntegerField(max_length=10)
	title = models.CharField(max_length=80)
	description = models.TextField()
	image = models.CharField(max_length=80)

	### Product in-stock?
	in_stock = models.BooleanField(default=True)

	### Date of product will be in stock
	back_order_till = models.DateField()

	### Unit price to customer
	price_unit = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit shipping price to customer
	price_shipping = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit cost to Thuzio
	cost_unit = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit shipping cost to Thuzio
	cost_shipping = models.DecimalField(max_digits=10, decimal_places=2)