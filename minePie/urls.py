from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from app.api import *

v1_api = Api(api_name='v1')
v1_api.register(MineResource())
v1_api.register(EmployeeResource())
v1_api.register(PointResource())
v1_api.register(AreaResource())
v1_api.register(LocationResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minePie.views.home', name='home'),
    #url(r'^minePie/', include('minePie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
