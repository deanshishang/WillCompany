#-*- coding:utf-8 -*-
from django.db import models

class Recipe(models.Model):
	name = models.CharField(u"菜品名称", max_length=50, unique=True)
	description = models.CharField(u"菜品描述", max_length=200, blank=True)
	rtype = models.ForeignKey("Rtype", verbose_name=u"菜的种类")
	discount = models.FloatField(u"折扣", default=1.0)
	rstatus = models.IntegerField(u"菜品状态", default=1) #1-yes 0-no
	price = models.IntegerField(u"单价")
	imgurl = models.ImageField(u"图片", upload_to="order", max_length=100)
	comments = models.FloatField(u"评价等级", default=4) #1.0-->5.0
	shelfdate = models.DateField(u"上架时间", auto_now_add=True)
	modify_time = models.DateTimeField(u"修改时间", auto_now=True) #last modify

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = u"菜谱管理"
class Rtype(models.Model):
	name = models.CharField(u"种类名称", max_length=50, unique=True)
	sequence = models.IntegerField(u"序列", default=9)

	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = u"菜品种类"

class Table(models.Model):
	tablenum = models.IntegerField(u"桌号", unique=True)
	personnum = models.IntegerField(u"人数", default=4)
	tstatus = models.IntegerField(u"桌子状态", default=0) #0-free 1-basy
	ttype = models.ForeignKey("Ttype", verbose_name=u"桌型")
	count = models.IntegerField(u"计数", default=50) 
	add_date = models.DateField(u"建立时间", auto_now_add=True)
	modify_time = models.DateTimeField(u"修改时间", auto_now=True) #last modify

	def __unicode__(self):
		return "%d" % self.tablenum
		
	class Meta:
		verbose_name_plural = u"桌子管理"

class Ttype(models.Model):
	name = models.CharField(u"桌型", max_length=50)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = u"桌子类型"

class Order(models.Model):
	status = models.IntegerField(u"订单状态", default=0) #0-未下单 1-已下单
	orderno = models.IntegerField(u"订单编号", default=-1)
	table = models.ForeignKey("Table", verbose_name=u"桌号",default=0)
	recipe = models.ManyToManyField("Recipe", verbose_name=u"菜品")
	add_time = models.DateTimeField(u"创建时间", auto_now_add=True)
	modify_time = models.DateTimeField(u"改单时间", auto_now=True)  #last modify

	def __unicode__(self):
		return "%d" % self.orderno

class Depot(models.Model):
	count = models.IntegerField(u"计数器", default=1)
	add_time = models.DateTimeField(u"创建时间", auto_now_add=True)
	modify_time = models.DateTimeField(u"修改时间", auto_now=True)
	order = models.ForeignKey("Order", verbose_name=u"订单", default=0)

	def __unicode__(self):
		return "%s" % self.add_time

class Detail(models.Model):
	depot = models.ForeignKey("Depot", verbose_name=u"订单")
	recipe = models.ForeignKey("Recipe", verbose_name=u"菜品")
	add_time = models.DateTimeField(u"建立时间", auto_now_add=True)

	def __unicode__(self):
		return self.recipe.name

class Phoneid(models.Model):
	phone = models.CharField(u"手机信息", max_length=50, unique=True)
	table = models.ForeignKey("Table", verbose_name=u"桌子信息")

	def __unicode__(self):
		return phone

class System(models.Model):
	hotel_name = models.CharField("饭店名称", max_length=100)
	hotel_address = models.CharField("饭店地址", max_length=100)

	def __unicode__(self):
		return hotel_name

	class Meta:
		verbose_name_plural = u"系统管理"
