from django.conf.urls import patterns, url
from django.http import HttpResponseRedirect
from admincp import views

urlpatterns = patterns('',
	url(r'^$', lambda r : HttpResponseRedirect('/admincp/index')),
	url(r'^index/$', views.index, name='index'),
	url(r'^(?P<product_id>\d+)/$', views.detail, name='detail'),
	url(r'^add_product/$', views.add_product, name='add_product'),
	url(r'^revenue/$', views.revenue, name='revenue'),
	url(r'^reporting_api/$', views.reporting_api, name='reporting_api'),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^logging_in/$', views.logging_in, name='logging_in'),
	url(r'^logging_out/$', views.logging_out, name='logging_out'),
	)