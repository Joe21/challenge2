import json, datetime
from django.shortcuts import get_object_or_404, render_to_response, Http404, redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from thuzioapp.models import Customer, Product, Purchase, ProductPurchase
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

# class IndexView(generic.ListView):
# 	template_name = 'admincp/index.html'
# 	context_object_name = 'all_products'

# 	def get_queryset(self):
# 		"""Return all products"""
# 		return Product.objects.all()
@login_required(login_url='/admincp/signin/')
@staff_member_required
def index(request):
	
	return render(request, 'admincp/index.html', {})

class DetailView(generic.DetailView):
	model = Product
	template_name = "admincp/detail.html"

@login_required(login_url='/admincp/signin/')
@staff_member_required
def revenue(request):
	sales = Purchase.objects.exclude(status=1)
	return render(request, 'admincp/revenue.html', {'sales':sales})

@login_required(login_url='/admincp/signin/')
@staff_member_required
def add_product(request):
	title = request.POST['title']
	description = request.POST['description']
	image_300x200 = request.POST['image_300x200']
	image_600x400 = request.POST['image_600x400']
	price_unit_normal = request.POST['price_unit_normal']
	price_shipping = request.POST['price_shipping']
	cost_unit = request.POST['cost_unit']
	cost_shipping = request.POST['cost_shipping']

	# new_product = Product()


	return render_to_response('admincp/index.html', {}, context_instance=RequestContext(request))

def signin(request):
	return render_to_response('admincp/signin.html', {}, context_instance=RequestContext(request))

def logging_in(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active and user.is_staff:
			login(request, user)
			return redirect('/admincp', permanent=True)
		else:
			raise Http404
	else:
		raise Http404