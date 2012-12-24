
from django.conf.urls.defaults import *
from models import *
from views import *

urlpatterns = patterns('',

    (r'book/create/$', create_book),
    (r'book/list/$', list_book ),
    (r'book/edit/(?P<id>[^/]+)/$', edit_book),
    (r'book/view/(?P<id>[^/]+)/$', view_book),
    
    (r'author/create/$', create_author),
    (r'author/list/$', list_author ),
    (r'author/edit/(?P<id>[^/]+)/$', edit_author),
    (r'author/view/(?P<id>[^/]+)/$', view_author),
    
    (r'publisher/create/$', create_publisher),
    (r'publisher/list/$', list_publisher ),
    (r'publisher/edit/(?P<id>[^/]+)/$', edit_publisher),
    (r'publisher/view/(?P<id>[^/]+)/$', view_publisher),
    
    (r'dean/$', my_test1),
)
