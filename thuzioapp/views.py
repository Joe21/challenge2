from django.shortcuts import render_to_response, render, get_object_or_404
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from thuzioapp.models import Customer, Product, Purchase
from django.contrib.auth.models import User

# GET request for index view
def index(request):
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

	# [DEBUGGING] check user authentication
	if request.user.is_authenticated():
		print '-=-=-=-=-=-=-=-=-=-=-'
		print 'user logged in'
		print '-=-=-=-=-=-=-=-=-=-=-'
	else:
		print '-=-=-=-=-=-=-=-=-=-=-'
		print'user not logged in'
		print '-=-=-=-=-=-=-=-=-=-=-'

	# [DEBUGGING] check shopping cart cache
	if 'shopping_cart' in request.session:
		print '-=-=-=-=-=-=-=-=-=-=-'
		print "shopping cart exists"
		print request.session['shopping_cart']
		print len(request.session['shopping_cart'])
		print '-=-=-=-=-=-=-=-=-=-=-'
	else:
		request.session['shopping_cart'] = []
		print '-=-=-=-=-=-=-=-=-=-=-'
		print 'shopping cart created'
		print request.session['shopping_cart']
		print len(request.session['shopping_cart'])
		print '-=-=-=-=-=-=-=-=-=-=-'

	return render_to_response('thuzioapp/index.html', {'products': products}, context_instance=RequestContext(request))

# GET request for detail view
def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)

	return render_to_response('thuzioapp/detail.html', {'product': product}, context_instance=RequestContext(request))

# Ensure user authentication
@login_required(login_url='/thuzioapp/signin/')
# GET request for checkout view
def checkout(request):

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
	# level = request.POST['level']
	address = request.POST['address']
	# zipcode = request.POST['zipcode']
	# cc_number = request.POST['cc_number']

	user = User.objects.create_user(username, email, password)
	user.save()
	user_id = user.pk
	customer = Customer(first_name=first_name, last_name=last_name, email_address=email, address=address, zipcode=55555, cc_number=1111222233334444, level=2, user_id=user_id)
	customer.save()

	return redirect('/thuzioapp')

# POST request to add product to session shopping cart
def add_to_cart(request):
	product_id = int(request.POST['product'])
	qty = int(request.POST['qty'])

	if request.session['shopping_cart'] is not None:

		for _ in range(qty):
			request.session['shopping_cart'].append(product_id)

		print '-=-=-=-=-=-=-=-=-=-=-'
		print request.session['shopping_cart']
		print '-=-=-=-=-=-=-=-=-=-=-'
		return redirect('/thuzioapp')
	else:
		request.session['shopping_cart'] = []
		request.session['shopping_cart'].append(product_id)
		return redirect('/thuzioapp')

	# product_info = [product_id, qty]

	# if request.session['shopping_cart'] is not None:
		
	# 	for i in request.session['shopping_cart']:
	# 		if i[0] == product_id:
	# 			i[1] += qty
	# 	else:
	# 		request.session['shopping_cart'].append(product_info)


		# for i in range(qty):
		# 	request.session['shopping_cart'].append(product_id)
		# 
		# request.session['shopping_cart'].append(product_info)

# POST request to remove product from session shopping cart
def remove_from_cart(request):
	product_id = int(request.POST['product'])
	qty = int(request.POST['qty'])

	if request.session['shopping_cart'] is not None:
		for i in range(qty):
			request.session['shopping_cart'].remove(product_id)
		
		print '-=-=-=-=-=-=-=-=-=-=-'
		print request.session['shopping_cart']
		print '-=-=-=-=-=-=-=-=-=-=-'
		return redirect('/thuzioapp')
	else:
		raise Http404

# GET request to cart view
def cart(request):

	if request.session['shopping_cart'] is not None:
		products = []
		for item in request.session['shopping_cart']:
			product = Product.objects.get(pk=item)
			product.qty = request.session['shopping_cart'].count(item)

			if not product in products:
				products.append(product)

		print products

	else:
		products = None
		print '-----------'
		print "cart empty"
		print '-----------'

	return render_to_response('thuzioapp/cart.html', {'products': products}, context_instance=RequestContext(request))

# GET request to about view
def about(request):

	return render(request, 'thuzioapp/about.html')