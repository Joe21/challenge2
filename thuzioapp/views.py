# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse

from thuzioapp.models import Customer, Product, Purchase
from django.contrib.auth.models import User

def index(request):
	all_products = Product.objects.order_by('model_number')[:5]
	context = {'all_products': all_products}
	return render(request, 'thuzioapp/index.html', context)

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'thuzioapp/detail.html', {'product': product})
	
def checkout(request):
	return HttpResponse("Checkout Page")

def complete(request):
	return HttpResponse("Purchase Complete")

# def testing(request):
# return HttpResponse("Details Page for product %s" % product_id)
	# if not request.user.is_authenticated():
