from django.conf.urls import patterns, url
from django.http import HttpResponseRedirect
from thuzioapp import views

urlpatterns = patterns('',
	url(r'^$', lambda r : HttpResponseRedirect('/thuzioapp/index')),
	url(r'^index/$', views.index, name='index'),
	url(r'^(?P<product_id>\d+)/$', views.detail, name='detail'),
	url(r'^checkout/$', views.checkout, name='checkout'),
	url(r'^complete/$', views.complete, name='complete'),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^logging_in/$', views.logging_in, name='logging_in'),
	url(r'^signout/$', views.signout, name='signout'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^create_new_account/$', views.create_new_account, name='create_new_account'),
	url(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart'),
	url(r'^cart/$', views.cart, name='cart'),
	url(r'^about/$', views.about, name='about'),
	)