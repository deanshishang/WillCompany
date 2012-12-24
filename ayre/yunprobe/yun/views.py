# Create your views here.
from django.http import HttpResponse
import traceback
from global_ import logger 
from handler import Handler
from transfer.packet import *
#from cache_ import *
import models

def entry(request):
	try:
		if request.method == 'GET':
			return HttpResponse('dfdfdfdfdf')
		if request.method == 'POST':
			data = request.raw_post_data
			logger.debug("The request data: %s" % data)
			header = {}
			retCode = Packet.unpackHeader(data, header)
			if retCode:
				logger.debug("header: %s %s %s %s"% (header['prover'], header['protype'],
					header['devicename'], header['valuelen']))

				reportDataList = Packet.unpackBody(header['valuelen'], header['value'])
				logger.debug("The reportDataList: %s" % reportDataList)
				data = Handler.handle(header['devicename'], reportDataList)
			return HttpResponse(data)
	except Exception, e:
		exstr = traceback.format_exc()
		logger.critical("%s" % str(exstr))
