from django.conf.urls import patterns, url
from thuzioapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<product_id>\d+)/$', views.detail, name='detail'),
	url(r'^checkout/$', views.checkout, name='checkout'),
	url(r'^complete$', views.complete, name='complete'),
	)