from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.template import RequestContext

def index(request):
	return HttpResponse("Index Page")

def detail(request, product_id):
	return HttpResponse("Details Page for product %s" % product_id)

def checkout(request):
	return HttpResponse("Checkout Page")

def complete(request):
	return HttpResponse("Purchase Complete")