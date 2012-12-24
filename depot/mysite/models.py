#-*- ecoding:utf-8 -*-
from django.db import models

class Book(models.Model):
	title = models.CharField("书名",max_length=100)
	author = models.ManyToManyField('Author')
	description = models.TextField('书籍描述')
	price = models.DecimalField('价钱',max_digits=8, decimal_places=2)
	image_url = models.ImageField('封面',upload_to="mysite", max_length=100, null=True, blank=True)
	publisher = models.ForeignKey('Publisher', related_name='publisher_book')
	pub_time = models.DateField('出版时间',auto_now_add=True)

	def __unicode__(self):
		return "%s" % self.title
class Author(models.Model):	
	name = models.CharField('作者姓名',max_length=100)
	age = models.IntegerField('作者年龄',max_length=100)
	email = models.EmailField('作者邮箱')

	def __unicode__(self):
		return "%s" % self.name
class Publisher(models.Model):
	name = models.CharField('出版商',max_length=100)
	phone = models.IntegerField('联系电话',max_length=20)
	
	def __unicode__(self):
		return "%s" % self.name
