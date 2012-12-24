from django.conf.urls import patterns, include, url
from order.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eryaeat.views.home', name='home'),
    # url(r'^eryaeat/', include('eryaeat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^order/', include("order.urls")),
	(r'^mydd/$', mydd),
	(r'^mydd/test/$', mytest),
	(r'^mana/$', mana),
)

from django.conf.urls.static import static
import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
