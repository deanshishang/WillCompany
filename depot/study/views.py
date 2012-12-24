from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from models import *

def hello(request):
	t = get_template("test/hello.html")
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))

