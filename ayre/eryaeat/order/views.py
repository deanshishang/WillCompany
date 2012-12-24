from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.template.loader import get_template
from models import *
def mydd(request):
	t = get_template('mytest.html')
	c = RequestContext(request, locals)
	return HttpResponse(t.render(c))

def mytest(request):
	t = get_template('mytest1.html')
	c = RequestContext(request, locals)
	return HttpResponse(t.render(c))

def mana(request):
	
	recipe = Recipe.objects.all()

	t = get_template('mana.html')
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))
