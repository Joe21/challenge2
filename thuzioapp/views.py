from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.template import RequestContext, loader

from thuzioapp.models import Customer, Product, Purchase


def index(request):
	all_products = Product.objects.order_by('model_number')[:5]
	template = loader.get_template('thuzioapp/testing.html')
	context = RequestContext(request, {
		'all_products': all_products, 
		})
	return HttpResponse(template.render(context))

def detail(request, product_id):
	return HttpResponse("Details Page for product %s" % product_id)

def checkout(request):
	return HttpResponse("Checkout Page")

def complete(request):
	return HttpResponse("Purchase Complete")

def testing(request):
	all_products = Product.objects.order_by('model_number')[:5]
	template = loader.get_template('thuzioapp/testing.html')
	context = RequestContext(request, {
		'all_products': all_products, 
		})
	return HttpResponse(template.render(context))