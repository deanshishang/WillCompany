#-*- coding:utf-8 -*-
from django.db import connection
import time, traceback

import models
from global_ import logger


class CacheDb:
	device = {}

	@staticmethod
	def syncAllFromDb():
		try:
			deviceList = []
			cursor = connection.cursor()
			sql = "select name,id from yun_hotel"
			cursor.execute(sql)
			row = cursor.fetchone()
			while row:
				device = {}
				device['name'] = row[0]
				device['id'] = row[1]
				deviceList.append(device)
				CacheDb.device[row[0]] = {"id":row[1]}
				row = cursor.fetchone()
		except Exception, e:
			exstr = traceback.format_exc()
			logger.critical("%s" % str(exstr))
	
	@staticmethod
	def getTaskList(deviceName, taskList):
		result = False
		if CacheDb.device.has_key(deviceName):
			result = True
#			taskDict={}
#			if CacheDb.device[deviceName].has_key('task')
#				taskDict = CacheDb.device[deviceName]['task']
#			#get task list
#			for key in taskDict.keys():
#				#check time
#				info = taskDict[key]
#				interval = info['interval']*60 # to second
#				curtime = int(time.time())
#				if (info['lasttime'] + interval) < curtime: #间隔时间已过
#					logger.debug("last:%d + interval:%d < curtime:%d" %(info['lasttime'], interval,curtime))
#					task = DetectTask(key, info['url'], info['ip'])
#					taskList.append(task)
#				else:
#					logger.debug("last:%d + interval:%d >= curtime:%d" %(info['lasttime'],interval,curtime))

		return result

CacheDb.syncAllFromDb()
