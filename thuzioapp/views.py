from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from thuzioapp.models import Customer, Product, Purchase
from django.contrib.auth.models import User

def index(request):
	# Local variable for API to DB for all Products order by model number 
	# all_products = Product.objects.order_by('model_number')[:5]
	all_products = Product.objects.order_by('model_number')
	context = {'all_products': all_products}

	# Used for debugging to check user authentication
	if request.user.is_authenticated():
		print '-=-=-=-=-=-=-=-=-=-=-'
		print 'user logged in'
		print '-=-=-=-=-=-=-=-=-=-=-'
	else:
		print '-=-=-=-=-=-=-=-=-=-=-'
		print'user not logged in'
		print '-=-=-=-=-=-=-=-=-=-=-'

	if 'shopping_cart' in request.session:
		print '-=-=-=-=-=-=-=-=-=-=-'
		print "shopping cart exists"
		print request.session['shopping_cart']
		print '-=-=-=-=-=-=-=-=-=-=-'
	else:
		request.session['shopping_cart'] = []
		print '-=-=-=-=-=-=-=-=-=-=-'
		print 'shopping cart created'
		print request.session['shopping_cart']
		print '-=-=-=-=-=-=-=-=-=-=-'

	return render(request, 'thuzioapp/index.html', context)

# GET request to view product 
def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'thuzioapp/detail.html', {'product': product})

# Ensure user authentication for checkout action
@login_required(login_url='/thuzioapp/signin/')
def checkout(request):

	# Used for debugging shoppingcart
	print '-=-=-=-=-=-=-=-=-=-=-'
	print request.session['new_purchase']
	print '-=-=-=-=-=-=-=-=-=-=-'

	return render(request, 'thuzioapp/checkout.html')

# Ensure user authentication for complete action
@login_required(login_url='/thuzioapp/signin/')
def complete(request):
	return render(request, 'thuzioapp/complete.html')

# GET request to view signin form 
def signin(request):
	return render(request, 'thuzioapp/signin.html')

# Handle POST request for user authentication *Need to add encryption in production*
def logging_in(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect('/thuzioapp')
		else:
			raise Http404
	else:
		raise Http404

# Handle POST request to signout
def signout(request):
	logout(request)
	return redirect('/thuzioapp')

# GET request to signup
def signup(request):
	return render(request, 'thuzioapp/signup.html')

# Handle POST request to create new user & customer
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
	product_id = request.POST['product']

	if request.session['shopping_cart'] is not None:
		request.session['shopping_cart'].append(product_id)
		print '-=-=-=-=-=-=-=-=-=-=-'
		print request.session['shopping_cart']
		print '-=-=-=-=-=-=-=-=-=-=-'
		return redirect('/thuzioapp')
	else:
		request.session['shopping_cart'] = []
		request.session['shopping_cart'].append(product_id)
		return redirect('/thuzioapp')