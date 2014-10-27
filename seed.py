# python manage.py loaddata fixture.json

# Create sample users: Note that these are not superusers,
# and they must till be added to customers until controllers automate this
from django.contrib.auth.models import User
from thuzioapp.models import Purchase, Customer, Product, ProductPurchase

joe = Customer(first_name="Joe", last_name="Jung", email_address = "joej21@gmail.com", address="123 drive", zipcode=12345, cc_number=1234567890123456, level=1, user_id=1)
joe.save()

jim = User.objects.create_user('Jim', 'jim@gmail.com', 'password')
jim.save()

jim = Customer(first_name="Jim", last_name="Jones", email_address = "jim@gmail.com", address="jim drive", zipcode=12345, cc_number=1111111111111111, level=1, user_id=2)
jim.save()


# 10/15/14 11:45pm - as of now, we're assuming the discount only applies for the merchandise
# price normal = 50.00
# 5% silver = 47.50
# 10% gold = 45.00
# 10% plat = 45.00

jeter = Product(model_number=1, title="Autographed Derek Jeter Card", description="2007 Topps Fleer Ultra autographed Derek Jeter Rookie Card. Card comes in a sealed protective case and a certificate of authenticity!", in_stock=True, price_unit_normal=50.00, price_unit_silver=47.50, price_unit_gold=45.00, price_unit_platinum=45.00, price_shipping=4.99, price_shipping_platinum=0.00, price_total_normal=54.99, price_total_silver=52.49, price_total_gold=45.00, price_total_platinum=45.00, cost_unit=40.00, cost_shipping=2.49, cost_total=42.49)
jeter.save()

tiki = Product(model_number=2, title="Autographed Tiki Barber Game Jersey", description="2002 Week 1 Tiki Barber Autographed game jersey. Comes with certificate of authenticity and an exclusive game card on Tiki's stats for that game!", in_stock = True, price_unit_normal=699.99, price_unit_silver=664.99, price_unit_gold=629.99, price_unit_platinum=629.99, price_shipping=5.99, price_shipping_platinum=0.00, price_total_normal=705.98, price_total_silver=670.98, price_total_gold=635.98, price_total_platinum=629.99, cost_unit=500.00, cost_shipping=3.99, cost_total=503.99)
tiki.save()

purchase1 = Purchase(customer_id=1, po_number=1, status=1, price_purchase=749.99, price_shipping=9.98, price_total=759.97, cost_purchase=400.00, cost_shipping=6.48, cost_total=406.48, revenue_total=353.49)
purchase1.save()

purchase2 = Purchase(customer_id=2, po_number=2, status=1)
purchase2.save()


joe = Customer.objects.get(pk=1)
jim = Customer.objects.get(pk=2)
jeter = Product.object.get(pk=1)
tiki = Product.objects.get(pk=2)

first_purchase = Purchase(customer=joe)
first_purchase.po_number = 1
first_purchase.save()

first_purchase.products = [tiki,jeter]
first_purchase.save()

second_purchase = Purchase(customer=jim, po_number=2)


--------------
from django.contrib.auth.models import User
from thuzioapp.models import Purchase, Customer, Product, ProductPurchase
joe = Customer.objects.get(pk=1)
prod1 = Product.objects.get(pk=1)
prod2 = Product.objects.get(pk=2)

new_purchase = Purchase(customer=joe, status=1)
new_purchase = Purchase.objects.get(pk=3)
new_purchase.save()

new_product_purchase = ProductPurchase.objects.create(product_id=product.id, purchase_id=new_purchase.id, qty=1)
new_product_purchase = ProductPurchase.objects.get(purchase_id = new_purchase.id)
bla = []





