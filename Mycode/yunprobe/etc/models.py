#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class DeviceStatus(models.Model):
	device_name = models.CharField("DeviceName", max_length=64)
	mac_address = models.CharField("MAC", blank=True, max_length=32)
	ip = models.CharField("IP", blank=True, max_length=32)	
	mask = models.CharField("Mask", blank=True, max_length=32)	
	gateway = models.CharField("GateWay", blank=True, max_length=32)	
	ldns = models.CharField("LDNS", blank=True, max_length=256)	
	os_version = models.CharField("OSVersion", blank=True, max_length=256)	
	app_version = models.CharField("AppVersion", blank=True, max_length=256)	
	update_time = models.DateTimeField(auto_now=True)	
	
	def __unicode__(self):
		return "%s" % self.device_name

class Hotel(models.Model):
	hotel_name = models.CharField("饭店名称", max_length=150, unique=True)
	address = models.CharField("地址", max_length=200)
	phone = models.CharField("联系方式", max_length=50, blank=True)
	longitude = models.CharField("经度", max_length=30, blank=True)
	latitude = models.CharField("纬度", max_length=30, blank=True)
	#task = models.ManyToManyField("Task")
	modify_user = models.CharField("最后更新", max_length=100, blank=True, default="system")
	modify_time = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s" % self.hotel_name

