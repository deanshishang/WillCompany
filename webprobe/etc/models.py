#coding=utf-8
from django.db import models


class Task(models.Model):
    ""
    url = models.URLField("URL", verify_exists=False)
    ip = models.IPAddressField("IP", blank=True)
    interval = models.IntegerField("间隔(秒)", default=600)
    task_policy=models.IntegerField("探测频率",max_length=1,blank=False)
    limit_size=models.IntegerField("最大读取长度KB",max_length=6,blank=False,default=0)
    limit_time=models.IntegerField("最大读取时间秒",max_length=6,blank=False,default=0)
    task_type=models.IntegerField("任务类型",max_length=1,blank=False)
    status=models.IntegerField("状态",max_length=1,blank=False)
    detectbegin=models.IntegerField("开始探测",max_length=5,blank=False)
    detectend=models.IntegerField("结束探测",max_length=5,blank=False)
    modify_user=models.CharField("最后更新",max_length=100,blank=False)
    modify_time = models.DateTimeField(auto_now=True)
    remark=models.CharField("备注",max_length=100,blank=True)
    
    def __unicode__(self):
        return self.url
    
    def _repr(self):
        return self.url

    
class Device(models.Model):
    ""
    name = models.CharField("主机名", max_length=32, unique=True)
    isp = models.CharField("运营商", max_length=20, blank=True,default='')
    region = models.CharField("大区", max_length=20, blank=True,default='')
    province = models.CharField("省", max_length=20, blank=True,default='')
    city = models.CharField("城市", max_length=20, blank=True,default='')
    loc = models.CharField("机房", max_length=200, blank=True,default='')
    ip = models.CharField("IP",max_length=32, blank=True,default='')
    mac_address = models.CharField("MAC", blank=True, max_length=17,default='')
    status=models.IntegerField("状态",max_length=1,blank=False,default=1)
    tasks = models.ManyToManyField(Task)
    modify_user = models.CharField("最后更新",max_length=100,blank=False,default='system')
    modify_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    def _repr(self):
        return self.name
    

    
class DeviceStatus(models.Model):
    device_name = models.CharField("DeviceName",max_length=32,blank=False)
    mac_address = models.CharField("MAC", blank=True, max_length=32)
    ip = models.CharField("IP", blank=True,max_length=32)
    mask = models.CharField("Mask", blank=True,max_length=32)
    gateway = models.CharField("GateWay", blank=True,max_length=32)
    ldns = models.CharField("LDNS", blank=True, max_length=256)
    os_version = models.CharField("OSVersion", blank=True, max_length=256)
    app_version = models.CharField("AppVersion", blank=True, max_length=64)
    update_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.device_id
    
    def _repr(self):
        return self.device_id


class DtData(models.Model):
    ""
    task_id = models.IntegerField("任务编号",max_length=8,blank=False)
    device_id = models.IntegerField("设备编号",max_length=8,blank=False)
    dttime = models.IntegerField('探测时间',max_length=5,blank=False,default=0)
    t_dnslookup = models.IntegerField('DNS解析时间',max_length=5,blank=False,default=0)
    ip_conn = models.IPAddressField('探测ip',blank=True)
    http_code = models.IntegerField('httpCode',max_length=8,blank=True)
    result_code = models.IntegerField('返回代码',max_length=8,blank=True)
    t_conned = models.IntegerField('连接时间',blank=True)
    t_firstbyte = models.IntegerField('第1字节时间',blank=True)
    t_download = models.IntegerField('下载时间',blank=True)
    l_object = models.IntegerField('目标大小',max_length=8,blank=True)
    add_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.task_id
    
    def _repr(self):
        return self.task_id


import models
from django.contrib import admin
admin.site.register(models.Device)
admin.site.register(models.Task)
admin.site.register(models.DeviceStatus)
admin.site.register(models.DtData)

