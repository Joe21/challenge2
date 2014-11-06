import json, datetime
from django.shortcuts import get_object_or_404, render_to_response, Http404, redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from thuzioapp.models import Customer, Product, Purchase, ProductPurchase
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

from django.http import JsonResponse

@login_required(login_url='/admincp/signin/')
@staff_member_required
def index(request):
	all_products = Product.objects.all()
	paginator = Paginator(all_products, 5)

	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render(request, 'admincp/index.html', { 'products': products })

@login_required(login_url='/admincp/signin/')
@staff_member_required
def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)

	return render(request, 'admincp/detail.html', { 'product': product })

@login_required(login_url='/admincp/signin/')
@staff_member_required
def add_product(request):

	if request.method == 'GET':
		last_product = Product.objects.latest('id')
		model_number = last_product.id + 1
		return render(request, 'admincp/add_product.html', {'model_number': model_number})
	
	elif request.method == 'POST':
		model_number = request.POST['model_number']
		title = request.POST['title']
		description = request.POST['description']
		image_300x200 = request.POST['image_300x200']
		image_600x400 = request.POST['image_600x400']
		price_unit_normal = round(float(request.POST['price_unit_normal']), 2)
		price_shipping = round(float(request.POST['price_shipping']), 2)
		cost_unit = round(float(request.POST['cost_unit']), 2)
		cost_shipping = round(float(request.POST['cost_shipping']), 2)
		in_stock = bool(request.POST['in_stock'])

		price_unit_silver = round((price_unit_normal * .95), 2)
		price_unit_gold = round((price_unit_normal * .9), 2)
		price_unit_platinum = round((price_unit_normal * .9), 2)
		price_shipping_platinum = 0 
		price_total_normal = round((price_unit_normal + price_shipping), 2)
		price_total_silver = round((price_unit_silver + price_shipping), 2)
		price_total_gold = round((price_unit_gold + price_shipping), 2)
		price_total_platinum = round((price_unit_platinum + price_shipping_platinum), 2)
		cost_total = round((cost_unit + cost_shipping), 2)

		# Created field will be instantiated from the model
		# Backorder will default null, and in_stock interaction needs to be built in or done thru edit functionality
		new_product = Product(model_number=model_number, title=title, description=description, image_300x200=image_300x200, image_600x400=image_600x400, in_stock=in_stock, price_unit_normal=price_unit_normal, price_unit_silver=price_unit_silver, price_unit_gold=price_unit_gold, price_unit_platinum=price_unit_platinum, price_shipping=price_shipping, price_shipping_platinum=price_shipping_platinum, price_total_normal=price_total_normal, price_total_silver=price_total_silver, price_total_gold=price_total_gold, price_total_platinum=price_total_platinum, cost_unit=cost_unit, cost_shipping=cost_shipping, cost_total=cost_total)
		new_product.save()

		return redirect('/admincp', permanent=True)

@login_required(login_url='/admincp/signin/')
@staff_member_required
def revenue(request):
	total_revenue = 0
	sales = Purchase.objects.exclude(status=1)
	for sale in sales:
		total_revenue += sale.revenue_total

	return render(request, 'admincp/revenue.html', {'sales':sales, 'total_revenue': total_revenue})

def reporting_api(request):
	sales = Purchase.objects.exclude(status=1)		
	data_array = [0,0,0,0]

	for sale in sales:
		if sale.customer.level == 1:
			data_array[0] += 1
		elif sale.customer.level == 2:
			data_array[1] += 1
		elif sale.customer.level == 3:
			data_array[2] += 1
		else:
			data_array[3] += 1

	response = JsonResponse(data_array, safe=False)
	return HttpResponse(response)


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

def logging_out(request):
	logout(request)
	return redirect('/admincp', permanent=True)