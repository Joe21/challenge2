from django.contrib import admin
from thuzioapp.models import Customer, Product, Purchase
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Purchase)

# class CustomerAdmin(admin.ModelAdmin):
	# fields = ['first_name', 'last_name']

# admin.site.register(Customer, CustomerAdmin)