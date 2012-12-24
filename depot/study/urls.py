from django.conf.urls import patterns, include, url
from models import *
from views import *

urlpatterns = patterns('',
	url(r'hello/$', hello),				
)
