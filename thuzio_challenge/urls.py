from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thuzio_challenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thuzioapp/', include('thuzioapp.urls', namespace="thuzioapp")),
    url(r'^admincp/', include('admincp.urls', namespace="admincp")),
    url(r'^admin/', include(admin.site.urls)),
)
