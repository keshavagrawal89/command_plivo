from django.conf.urls import patterns, include, url
import os
from django.views.generic import TemplateView
from plivo_annyang.views import *
site_media = os.path.join(
     os.path.dirname(__file__), 'site_media'
   )
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', main_page),
	(r'^master_server/$', master_server),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
    # Examples:
    # url(r'^$', 'annyang.views.home', name='home'),
    # url(r'^annyang/', include('annyang.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
