from django.shortcuts import render_to_response, render, get_object_or_404
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from thuzioapp.models import Customer, Product, Purchase, ProductPurchase
from django.contrib.auth.models import User

# GET request for index view
def index(request):

	if 'shopping_cart' in request.session:
		print "shopping cart exists"
	else:
		request.session['shopping_cart'] = []
		print 'shopping cart created'

	# Check for customer membership level
	if request.user.is_authenticated():
		customer_id = request.user.pk
		customer = Customer.objects.get(pk=customer_id)
		level = customer.level
	else:
		level = None

	# Paginator
	all_products = Product.objects.order_by('model_number')
	paginator = Paginator(all_products, 10)

	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render_to_response('thuzioapp/index.html', {'products': products, 'level': level }, context_instance=RequestContext(request))

# GET request for detail view
def detail(request, product_id):

	if 'shopping_cart' in request.session:
		print "shopping cart exists"
	else:
		request.session['shopping_cart'] = []
		print 'shopping cart created'

	# Check for customer membership level
	if request.user.is_authenticated():
		customer_id = request.user.pk
		customer = Customer.objects.get(pk=customer_id)
		level = customer.level
	else:
		level = None

	product = get_object_or_404(Product, pk=product_id)

	return render_to_response('thuzioapp/detail.html', {'product': product, 'level': level}, context_instance=RequestContext(request))

# Ensure user authentication
@login_required(login_url='/thuzioapp/signin/')
# GET request for checkout view
def checkout(request):

	# Fetch customer
	customer_id = request.user.pk
	customer = Customer.objects.get(pk=customer_id)
	level = customer.level

	# Create new PO
	new_purchase = Purchase(customer=customer, status=1)
	new_purchase.save()

	# # Fetch shopping cart from cache
	shopping_cart = request.session['shopping_cart']

	for item in shopping_cart:
		product = Product.objects.get(pk=item)

		if product in new_purchase.products.all():
			print "already in there"
		else:
			new_product_purchase = ProductPurchase.objects.create(product_id=product.id, purchase_id=new_purchase.id, qty=1)

	print new_purchase.products.all()


		# if product in new_purchase.products.all():
		# 	# index = new_purchase.products.all().index[product]
		# 	# existing_product = new_purchase.products.all()[index]
		# 	# updated_qty = existing_product.qty + 1
		# 	# existing_product.update(qty=updated_qty)
		# 	print "this product exists so we are adding it"
		# 	update_product = new_purchase.products.get(id=product.id)
		# 	# updated_qty = update_product.qty + 1
		# 	# print "updated qty: " + str(updated_qty)
		# 	# new_purchase.products.filter(id=product.id).update(qty=updated_qty)
		# 	update_product.qty += 1
		# 	print str(update_product.title) + ' has been updated'
		# 	print str(update_product.qty)
		# else:
		# 	new_purchase.products.add(product)
		# 	print str(product.title) + ' was newly added'

	# new_purchase.save()


	# print new_purchase.products.all()[0].qty

			# increment_this_product = new_purchase.products.get(pk=product.pk)
			# increment_this_product.qty +=1
			# increment_this_product.update(qty=increment_this_product.qty)
			# print "product: " + str(increment_this_product.model_number)
			# print "qty :" + str(increment_this_product.qty)
			# new_purchase.save()

	request.session['purchase'] = new_purchase.pk

	return render(request, 'thuzioapp/checkout.html')

# Ensure user authentication
@login_required(login_url='/thuzioapp/signin/')
# GET request for complete view
def complete(request):

	return render(request, 'thuzioapp/complete.html')

# GET request for signin view 
def signin(request):

	return render_to_response('thuzioapp/signin.html', {}, context_instance=RequestContext(request))

# POST request for user authentication *Need to add encryption in production*
def logging_in(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect('/thuzioapp', permanent=True)
		else:
			raise Http404
	else:
		raise Http404

# POST request to signout view
def signout(request):
	logout(request)
	return redirect('/thuzioapp', permanent=True)

# GET request to signup view
def signup(request):
	return render_to_response('thuzioapp/signup.html', {}, context_instance=RequestContext(request))

# POST request to create new user & customer
def create_new_account(request):

	username = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	level = request.POST['level']
	address = request.POST['address']
	zipcode = request.POST['zipcode']
	cc_number = request.POST['cc_number']
	if len(cc_number) == 16:
		cc_number = request.POST['cc_number']
	else:
		cc_number = None

	user = User.objects.create_user(username, email, password)
	user.save()
	user_id = user.pk
	customer = Customer(first_name=first_name, last_name=last_name, email_address=email, address=address, zipcode=55555, cc_number=cc_number, level=level, user_id=user_id)
	customer.save()

	return redirect('/thuzioapp')

# POST request to add product to session shopping cart
def add_to_cart(request):
	product_id = int(request.POST['product'])
	qty = int(request.POST['qty'])

	if request.session['shopping_cart'] is not None:
		for _ in range(qty):
			request.session['shopping_cart'].append(product_id)
		return redirect('/thuzioapp')
	else:
		request.session['shopping_cart'] = []
		for _ in range(qty):
			request.session['shopping_cart'].append(product_id)
		return redirect('/thuzioapp')

# POST request to remove product from session shopping cart
def remove_from_cart(request):
	product_id = int(request.POST['product'])
	qty = int(request.POST['qty'])

	if request.session['shopping_cart'] is not None:
		for i in range(qty):
			request.session['shopping_cart'].remove(product_id)		
		return redirect('/thuzioapp')
	else:
		raise Http404

# GET request to cart view
def cart(request):

	if 'shopping_cart' in request.session:
		print "shopping cart exists"
	else:
		request.session['shopping_cart'] = []
		print 'shopping cart created'

	# Check for customer membership level
	if request.user.is_authenticated():
		customer_id = request.user.pk
		customer = Customer.objects.get(pk=customer_id)
		level = customer.level
	else:
		level = None

	if len(request.session['shopping_cart']) > 0:
		products = []
		for item in request.session['shopping_cart']:
			product = Product.objects.get(pk=item)
			product.qty = request.session['shopping_cart'].count(item)

			if not product in products:
				products.append(product)

		print products

	else:
		products = None

	return render_to_response('thuzioapp/cart.html', {'products': products, 'level':level}, context_instance=RequestContext(request))

# GET request to about view
def about(request):

	return render(request, 'thuzioapp/about.html')



###### Debugging ######
## Copy, Paste, & Uncomment accordingly to use

# User Login status
# if request.user.is_authenticated():
# 	print '-=-=-=-=-=-=-=-=-=-=-'
# 	print 'user logged in'
# 	print '-=-=-=-=-=-=-=-=-=-=-'
# else:
# 	print '-=-=-=-=-=-=-=-=-=-=-'
# 	print'user not logged in'
# 	print '-=-=-=-=-=-=-=-=-=-=-'

# Shopping cart status
# if 'shopping_cart' in request.session:
# 	print '-=-=-=-=-=-=-=-=-=-=-'
# 	print "shopping cart exists"
# 	print request.session['shopping_cart']
# 	print len(request.session['shopping_cart'])
# 	print '-=-=-=-=-=-=-=-=-=-=-'
# else:
# 	request.session['shopping_cart'] = []
# 	print '-=-=-=-=-=-=-=-=-=-=-'
# 	print 'shopping cart created'
# 	print request.session['shopping_cart']
# 	print len(request.session['shopping_cart'])
# 	print '-=-=-=-=-=-=-=-=-=-=-'



