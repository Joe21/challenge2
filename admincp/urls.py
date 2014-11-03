from django.conf.urls import patterns, url
from django.http import HttpResponseRedirect
from admincp import views

# urlpatterns = patterns('',
# 	url(r'^$', lambda r : HttpResponseRedirect('/admincp/index')),
# 	url(r'^index/$', views.index, name='index'),
# 	url(r'^signin/$', views.signin, name='signin'),
# 	url(r'^logging_in/$', views.logging_in, name='logging_in'),
# 	url(r'^review/$', views.review, name='review'),
# 	)

urlpatterns = patterns('',
	url(r'^$', lambda r : HttpResponseRedirect('/admincp/index')),
	url(r'^index/$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^revenue/$', views.revenue, name='revenue'),
	)