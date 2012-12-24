#-*- coding:utf-8 -*-
from django.db import models

class Order(models.Model):
	name = models.CharField(max_length=50)
	address = models.TextField()
	email = models.EmailField()

	def __unicode__(self):
		return "%s" % self.name
class Product(models.Model):
	title = models.CharField(max_length=100, unique=True)
	description = models.TextField()
	imag_url = models.URLField(max_length=200)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	date_available = models.DateField()
	orders = models.ManyToManyField(Order, through='LineItem')

	def __unicode__(self):
		return "%s" % self.title


class LineItem(models.Model):
	product = models.ForeignKey(Product)
	order = models.ForeignKey(Order,verbose_name="order")
	unit_price = models.DecimalField(max_digits=8, decimal_places=2)
	quantity = models.IntegerField()

	def __unicode__(self):
		return "%s" %self.product.title
