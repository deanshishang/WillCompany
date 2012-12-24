#!/usr/bin/env python


import traceback
from django.http import HttpResponse
from handler import Handler
from transfer.packet import *
from global_ import logger


def entry(request):
    
    if request.method == 'GET':
        return HttpResponse("KAO")
    elif request.method == 'POST':
        
        try:
            #TODO: check MAC
            #logger.info("Remote %s request" % str(request.META['REMOTE_ADDR']))
            #get post data
            data = request.raw_post_data;
            #unpack data
			#print "\n#####################\n"
			#print data
			#print "\n#####################\n"


            header={}
            retcode = Packet.unpackHeader(data,header)
            
            if retcode:
                
                logger.debug("header: %s %s %s %s" % \
                             (header['prover'],header['protype'],
                              header['devicename'],header['valuelen']))
                
                reportDataList = Packet.unpackBody(header['valuelen'],header['value'])
                
                data = Handler.handle(header['devicename'], reportDataList)
                
                return HttpResponse(data)
            else:
                return HttpResponse("Bad Packet")
        
        except Exception,e:
            exstr = traceback.format_exc()
            logger.critical("%s" % str(exstr))
