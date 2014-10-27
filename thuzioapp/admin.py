from django.contrib import admin
from thuzioapp.models import Customer, Product, Purchase, ProductPurchase
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(ProductPurchase)

# class CustomerAdmin(admin.ModelAdmin):
	# fields = ['first_name', 'last_name']

# admin.site.register(Customer, CustomerAdmin)