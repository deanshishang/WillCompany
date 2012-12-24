from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from depotapp.views import login_view, logout_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'depot.views.home', name='home'),
    # url(r'^depot/', include('depot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$', login_view),
	url(r'^accounts/logout/$', logout_view),
)

urlpatterns += patterns('', url(r'^depotapp/', include('depotapp.urls')),)
urlpatterns += patterns('', url(r'^mysite/', include('mysite.urls')),)
urlpatterns += patterns('', url(r'^study/', include('study.urls')),)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#This will work if DEBUG is True.
urlpatterns += staticfiles_urlpatterns()

import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
