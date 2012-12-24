from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('webprobe',
    # Example:
    # (r'^webprobe/', include('webprobe.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
    (r'^admin/(.*)', include(admin.site.urls)),
    (r'^detect/$','detect.view.entry')
)
