# Initial plan to use forms has been benched due to mathematical calculations required.
# Future steps: create init functions which will perform the same "controller actions" to populate prices and costs
# but scope them internally within the model's instantiation process.


# from django import forms
# from thuzioapp.models import Product
# from django.utils import timezone
# import datetime

# class ProductForm(forms.ModelForm):
# 	model_number = forms.IntegerField(max_length=10)
# 	title = forms.CharField(max_length=80)
# 	description = forms.TextField()
# 	image_300x200 =	forms.CharField(max_length=200, default="http://prairieceramics.com/wpress/here/wp-content/uploads/2013/10/cache/image_coming_soon-300x200.jpg")
# 	image_600x400 = forms.CharField(max_length=200, default="http://placekitten.com/g/600/400")
# 	qty = forms.IntegerField(max_length=10, default=0, null=True)
# 	created = forms.DateField(default=datetime.datetime.now(), blank=True)
# 	in_stock = forms.BooleanField(default=True)
# 	back_order_till = forms.DateField(null=True)
# 	price_unit_normal = forms.DecimalField(max_digits=10, decimal_places=2)
# 	price_unit_silver = forms.DecimalField(max_digits=10, decimal_places=2)
# 	price_unit_gold = forms.DecimalField(max_digits=10, decimal_places=2)
# 	price_unit_platinum = forms.DecimalField(max_digits=10, decimal_places=2)
# 	price_shipping = forms.DecimalField(max_digits=10, decimal_places=2)
# 	price_shipping_platinum = forms.DecimalField(max_digits=10, decimal_places=2, default=0.00)
# 	price_total_normal = forms.DecimalField(max_digits=10, decimal_places=2)
# 	price_total_silver = forms.DecimalField(max_digits=10, decimal_places=2)
# 	price_total_gold = forms.DecimalField(max_digits=10, decimal_places=2)
# 	price_total_platinum = forms.DecimalField(max_digits=10, decimal_places=2)
# 	cost_unit = forms.DecimalField(max_digits=10, decimal_places=2)
# 	cost_shipping = forms.DecimalField(max_digits=10, decimal_places=2)
# 	cost_total = forms.DecimalField(max_digits=10, decimal_places=2) 
	

# 	class Meta:
# 		model = Product
# 		fields = ('title', 'description', 'image_300x200', 'image_600x400', 'in_stock', 'back_order_till', 'price_unit_normal', 'price_shipping', 'cost_unit', 'cost_shipping',)

# 		# exclude (model_number, back_order_till, price_unit_silver, price_unit_gold, price_unit_platinum, price_shipping_platinum, price_total_normal, price_total_silver, price_total_gold, price_total_platinum, cost_total)