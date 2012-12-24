from django.db import connection
import models
from cache_ import *
from transfer.packet import *
from transfer.report import *

class Handler:
	@classmethod
	def handle(self, deviceName, reportDataList):
		taskList = []
		for reportData in reportDataList:
			if reportData['t'] == rpt_login_tag:
				lgnRpt = LoginReport()
				lgnRpt.unpack(reportData['l'], reportData['v'])
				taskList = self.handleLogin(deviceName, lgnRpt)
#			elif reportData['t'] == rpt_detect_tag:
#				detRpt = DetectReport()
#				detRpt.unpack(reportData['l'], reportData['v'])
#				taskList = self.handleDetect(deviceName, detRpt)
			else:
				return "NOT SUPPORT"
  		retData = ""
		#for task in taskList
		#	data = task.pack()
		#	retData += Tlv.pack(det_task_tag, data)
		return Packet.packHeader(retData)
	@classmethod
	def handleLogin(self, deviceName, lgnRpt):
		taskList = []
		lgnHandler = LoginHandler()
		if not CacheDb.getTaskList(deviceName, taskList):
			lgnHandler.insertDbHotel(deviceName, lgnRpt)
		lgnHandler.insertDbDeviceStatus(deviceName, lgnRpt)

		return taskList

class LoginHandler:
	def __init__(self):
		pass

	def handle(self):
		pass

	def insertDbHotel(self, deviceName, lgnRpt):
		device = models.Hotel(name=deviceName)
		device.save()

	def insertDbDeviceStatus(self, deviceName, lgnRpt):
		deviceStatus = models.DeviceStatus(device_name=deviceName,mac_address=lgnRpt.mac,
				ip=lgnRpt.ip, mask=lgnRpt.mask, gateway=lgnRpt.gateway, ldns=lgnRpt.ldns,
				os_version=lgnRpt.osver, app_version=lgnRpt.appver)
		deviceStatus.save()
