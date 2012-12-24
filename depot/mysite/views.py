
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *


def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()

    t = get_template('mysite/create_book.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_book(request):
  
    list_items = Book.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('mysite/list_book.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_book(request, id):
    book_instance = Book.objects.get(id = id)

    t=get_template('mysite/view_book.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_book(request, id):

    book_instance = Book.objects.get(id=id)

    form = BookForm(request.POST or None, instance = book_instance)

    if form.is_valid():
        form.save()

    t=get_template('mysite/edit_book.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AuthorForm()

    t = get_template('mysite/create_author.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_author(request):
  
    list_items = Author.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('mysite/list_author.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_author(request, id):
    author_instance = Author.objects.get(id = id)

    t=get_template('mysite/view_author.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_author(request, id):

    author_instance = Author.objects.get(id=id)

    form = AuthorForm(request.POST or None, instance = author_instance)

    if form.is_valid():
        form.save()

    t=get_template('mysite/edit_author.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_publisher(request):
    form = PublisherForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PublisherForm()

    t = get_template('mysite/create_publisher.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_publisher(request):
  
    list_items = Publisher.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('mysite/list_publisher.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_publisher(request, id):
    publisher_instance = Publisher.objects.get(id = id)

    t=get_template('mysite/view_publisher.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_publisher(request, id):

    publisher_instance = Publisher.objects.get(id=id)

    form = PublisherForm(request.POST or None, instance = publisher_instance)

    if form.is_valid():
        form.save()

    t=get_template('mysite/edit_publisher.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))



def my_test1(request):

	book = Book.objects.all()

	t = get_template('mysite/dean.html')
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))
