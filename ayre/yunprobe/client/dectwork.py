import time, os, sys, socket, traceback
from urlparse import urlparse
from transfer.report import *
import httplib, urllib

from client.global_ import *


class DectWork:
	def __init__(self):
		self.device = {}
		self.keepAliveTime = 0

	def process(self):
		"""
			1) login and keep alive
		"""
		logger.info("dect work process ......")
		retCode = 0
		while retCode is not 200:
			logger.info("login to %s ......" % Global.serverAddress)
			retCode, retData = self.login()
			if retCode is 200:
				logger.info("login to %s ok" % Global.serverAddress)
				logger.debug("The retData: %s" % retData)
				self.keepAliveTime = time.time()
				self.handleResponse(retData)
				break;
			else:
				logger.info("loggin to %s faild %d" % (Global.serverAddress, int(retCode)))
			time.sleep(30)

		self.work()
	def login(self):
		retCode = 0
		retData = None
		retHeader = None
		try:
			deviceInfo={}
			self.getDeviceInfo(deviceInfo)
			rpt = LoginReport()
			senddata = rpt.packWithHeader(deviceInfo)
			retCode, retHeader, retData = self.report(Global.serverAddress, senddata)
		except Exception, e:
			exstr = traceback.format_exc()
			logger.critical("%s" % str(exstr))
		return retCode, retData

	def report(self, server, data):
		connected = False
		retCode = 0
		retHeader = None
		retData = None

		comp = urlparse(server)
		conn = None

		try:
			headers = {'Connection':'Keep-Alive'}
			tmp=""
			if comp.port is not None:
				tmp = comp.hostname+':%d' % comp.port
			else:
				tmp = como.hostname
			conn = httplib.HTTPConnection(tmp, timeout=10)
			conn.connect()
			connected = True
			conn.request(method="POST", url=comp.path, body=data, headers = headers)

			response = conn.getresponse()
			retCode = response.status
			retHeader = response.getheaders()
			retData = response.read()
		except Exception, e:
			exstr = traceback.format_exc()
			logger.critical("%s" % str(exstr))

		if connected and conn is not None:
			conn.close()

		return retCode, retHeader, retData

	def handleResponse(self, retdata):
		header = {}
		ret = Packet.unpackHeader(retdata, header)
		

	def getDeviceInfo(self, info):
		hostname = socket.gethostname()
		iplist = socket.gethostbyaddr(hostname)
	
		info['os'] = sys.platform
		info['mac'] = '00-22-fa-60-a4-5c'
		info['ip'] = iplist[2][0]
		info['mask'] = '225.255.255.0'
		info['gateway'] = '127.0.0.1'
		info['ldns'] = '127.0.0.1'
		info['app'] = Global.appVer

	def keepAlive(self):
		retCode, retData = self.login()
		return retCode, retData

	def work(self):
		while 1:
			if (self.keepAliveTime + Global.keepAliveInterval) < time.time():
				logger.info("Keep alive to %s......" % Global.serverAddress)
				retCode, retData =  self.keepAlive()
				if int(retCode) is 200:
					logger.info("Keep alive to %s ok" % Global.serverAddress)
					self.handleResponse(retData)
				else:
					logger.error("Keep alive to %s failed %d" % (Global.serverAddress, int(retCode)))
				self.keepAliveTime = time.time()

			time.sleep(1)
				
