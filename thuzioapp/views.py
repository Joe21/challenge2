from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



from thuzioapp.models import Customer, Product, Purchase
from django.contrib.auth.models import User


# TEMPLATE VIEWS

def index(request):
	all_products = Product.objects.order_by('model_number')[:5]
	context = {'all_products': all_products}

	if request.user.is_authenticated():
		print 'yes'
	else:
		print'no'
	# new_purchase = {}
	# new_purchase['user'] = 
	# request.session['new_purchase'] = new_purchase

	return render(request, 'thuzioapp/index.html', context)

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'thuzioapp/detail.html', {'product': product})

@login_required(login_url='/thuzioapp/login/')
def checkout(request):
	return render(request, 'thuzioapp/checkout.html')

@login_required(login_url='/thuzioapp/login/')
def complete(request):
	return render(request, 'thuzioapp/complete.html')

def signin(request):
	return render(request, 'thuzioapp/signin.html')

# ACTIONS
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
			# Return a 'disabled account' error message
	else:
		raise Http404
		# Return an 'invalid login' error message

def logging_out(request):
	logout(request)
	return redirect('/thuzioapp')
	# Redirect to a success page
