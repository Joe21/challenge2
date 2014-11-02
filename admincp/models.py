from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from thuzioapp.models import Customer, Product, Purchase, ProductPurchase
from django.contrib.auth.models import User