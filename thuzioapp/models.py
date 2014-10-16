from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User

class Customer(models.Model):
	# Customer extends from User
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

class Product(models.Model):
	# Fields for Product model
	model_number = models.IntegerField(max_length=10)
	title = models.CharField(max_length=80)
	description = models.TextField()
	image = models.CharField(max_length=80)

	### Product in-stock?
	in_stock = models.BooleanField(default=True)

	### Date of product will be in stock
	back_order_till = models.DateField(null=True)

	### Unit price to regular customer
	price_unit_normal = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit price to silver customer
	price_unit_silver = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit price to gold customer
	price_unit_gold = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit price to platinum customer
	price_unit_platinum = models.DecimalField(max_digits=10, decimal_places=2)

	### Shipping price to customers 
	price_shipping = models.DecimalField(max_digits=10, decimal_places=2)

	### Shipping price to platinum customers
	price_shipping_platinum = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

	### Total unit price to normal customer
	price_total_normal = models.DecimalField(max_digits=10, decimal_places=2)

	### Total unit price to silver customer
	price_total_silver = models.DecimalField(max_digits=10, decimal_places=2)

	### Total unit price to gold customer
	price_total_gold = models.DecimalField(max_digits=10, decimal_places=2)

	### Total unit price to platinum customer
	price_total_platinum = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit cost to Thuzio
	cost_unit = models.DecimalField(max_digits=10, decimal_places=2)

	### Unit shipping cost to Thuzio
	cost_shipping = models.DecimalField(max_digits=10, decimal_places=2)

	### Total unit cost to Thuzio
	cost_total = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return "Model# {}".format(self.model_number)


class Purchase(models.Model):
	# Purchase has a customer ID
	customer = models.ForeignKey(Customer, null=True)

	# Purchase and Product have many to many relationship
	# (One Purchase has many products, a product is reusable between Purchases)
	products = models.ManyToManyField(Product, null=True)

	# Fields for Purchase model
	###	Purchase Order number must remain unique
	po_number = models.IntegerField(max_length = 10, unique=True, null=True)

	### Choice field for purchase status
	STATUS = (
		(1, 'Incomplete'),
		(2, 'Processing'),
		(3, 'Shipped'),
		(4, 'Cancelled'),
		(5, 'Return/Refund'),
		(6, 'Complete')
		)
	status = models.IntegerField(max_length=1, choices=STATUS, default=1)

	### Total price of purchase to customer
	price_purchase = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Shipping price of purchase to customer
	price_shipping = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Total price on invoice to customer
	price_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	
	### Total cost of purchase to Thuzio
	cost_purchase = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Shipping cost of purchase to Thuzio
	cost_shipping = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Total cost of purchase to Thuzio
	cost_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	### Total revenue of purchase to Thuzio
	revenue_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	def __unicode__(self):
		return "PO# {}".format(self.po_number)
