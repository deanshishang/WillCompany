import datetime
# Create your views here.
from djangorestframework.views import View
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *


def create_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()

    t = get_template('depotapp/create_order.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_order(request):
  
    list_items = Order.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('depotapp/list_order.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_order(request, id):
    order_instance = Order.objects.get(id = id)

    t=get_template('depotapp/view_order.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_order(request, id):

    order_instance = Order.objects.get(id=id)

    form = OrderForm(request.POST or None, instance = order_instance)

    if form.is_valid():
        form.save()

    t=get_template('depotapp/edit_order.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_lineitem(request):
    form = LineItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LineItemForm()

    t = get_template('depotapp/create_lineitem.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_lineitem(request):
  
    list_items = LineItem.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('depotapp/list_lineitem.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_lineitem(request, id):
    lineitem_instance = LineItem.objects.get(id = id)

    t=get_template('depotapp/view_lineitem.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_lineitem(request, id):

    lineitem_instance = LineItem.objects.get(id=id)

    form = LineItemForm(request.POST or None, instance = lineitem_instance)

    if form.is_valid():
        form.save()

    t=get_template('depotapp/edit_lineitem.html')
    c=RequestContext(request,locals())

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    t = get_template('depotapp/create_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def list_product(request):
  
    list_items = Product.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('depotapp/list_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_product(request, id):
    product_instance = Product.objects.get(id = id)

    t=get_template('depotapp/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_product(request, id):

    product_instance = Product.objects.get(id=id)

    form = ProductForm(request.POST or None, instance = product_instance)

    if form.is_valid():
        form.save()

    t=get_template('depotapp/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))



def store_view(request):
#	products = Product.objects.filter(date_available__gt=datetime.datetime.now().date()).order_by("-date_available")
	products = Product.objects.all()
	cart = request.session.get("cart", None)
	if not cart:
		cart = Cart()
		request.session["cart"] = cart
	t = get_template('depotapp/store.html')
	c = RequestContext(request, locals())
	#return HttpResponse(cart.total_price)	
	return HttpResponse(t.render(c))

class Cart(object):
	def __init__(self, *args, **kwargs):
		self.items = []
		self.total_price = 0
	def add_product(self, product):
		self.total_price += product.price
		for item in self.items:
			if item.product.id == product.id:
				item.quantity += 1
				return
		self.items.append(LineItem(product=product, unit_price=product.price, quantity=1))

def view_cart(request):
	cart = request.session.get("cart", None)
	t = get_template('depotapp/view_cart.html')

	if not cart:
		cart = Cart()
		request.session["cart"] = cart
	
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))

def add_to_cart(request, id):
	product = Product.objects.get(id=id)
	cart = request.session.get("cart", None)
	if not cart:
		cart = Cart()
		request.session["cart"] = cart
	cart.add_product(product)
	request.session["cart"] = cart
	return view_cart(request)
def clean_cart(request):
	request.session['cart'] = Cart()
	return view_cart(request)

class RESTForCart(View):
	def get(self, request, *args, **kwargs):
		#cart = request.session.get('cart', Cart())
		return request.session['cart'].items
	def post(self, request, *args, **kwargs):
		print request.POST['product']
		product = Product.objects.get(id=request.POST['product'])
		cart = request.session['cart']
		cart.add_product(product)
		request.session['cart'] = cart
		return request.session['cart'].items
