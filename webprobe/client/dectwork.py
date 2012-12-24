'''

'''
import time,sys,os,socket,traceback
from urlparse import urlparse
import httplib, urllib

from client.global_ import *
from transfer.report import *
from transfer.task import *
from common.detect import *

class DectWork:
    '''
    '''
    
    def __init__(self):
        '''
        '''
        self.device = {} 
        self.dectTaskList=[]
        self.dectReportList=[]
        self.keepAliveTime = 0
        self.sendReportTime = 0
    
    def process(self):
        '''
            1) login and keep alive
            2) dect tasks
            3) report dect reult 
        '''
        logger.info("dect work process ...")
        
        retCode = 0
        while retCode is not 200:
            logger.info("login to %s ..." % Global.serverAddress )
            retCode,retData = self.login()
            if retCode is 200:
                logger.info("login to %s ok" % Global.serverAddress )
                self.keepAliveTime = time.time()
                self.handleResponse(retData)
                break;
            else:
                logger.error("login to %s failed %d" % (Global.serverAddress,int(retCode)))
            time.sleep(30)
            
        #loop 
        self.work()
           
    def work(self):
        '''
        '''
        while 1:
       
            #detect
            taskNum = len(self.dectTaskList)
            if taskNum is not 0:
                detTask = self.dectTaskList.pop()
                if detTask is not None:
                    httpDetect = HttpDetect()
                    detectDict = httpDetect.do(detTask.url)
                    detectDict['id'] = detTask.id   
                    logger.debug("Detct: %s %s (%d %d %d %d %d) %d %d" % \
                                 (detTask.url,detectDict['urlip'],
                                  detectDict['t_dnslookup'],detectDict['t_connected'],
                                  detectDict['t_firstbyte'],detectDict['t_download'],
                                  detectDict['l_object'],
                                  detectDict['httpCode'],detectDict['retCode']) )
                    detRpt = DetectReport(detectDict)
                    self.dectReportList.append(detRpt)
                    
            # send report
            if (self.sendReportTime + Global.sendReportInterval) < time.time():
                retCode,retData = self.sendReport()
                if int(retCode) is 200:
                    self.handleResponse(retData)
                self.sendReportTime = time.time()
                
            # send KeepAlive
            if (self.keepAliveTime + Global.keepAliveInterval) < time.time():
                logger.info("keep alive to %s ..." % Global.serverAddress )
                retCode,retData = self.keepAlive()
                if int(retCode) is 200:
                    logger.info("keep alive to %s ok" % Global.serverAddress )
                    self.handleResponse(retData)
                else:
                    logger.error("keep alive to %s failed %d" % (Global.serverAddress,int(retCode)))
                self.keepAliveTime = time.time()
                
            time.sleep(1)
         
    def login(self):
        '''
        '''
        retCode=0
        retHeader=None
        retData=None
        try:
            deviceInfo={}
            self.getDeviceInfo(deviceInfo)
            rpt = LoginReport()
            senddata = rpt.packWithHeader(deviceInfo)

#			print "##########################\n"
#			print "\n##########################"

            retCode,retHeader,retData = self.report(Global.serverAddress,senddata)
		#print senddata
        except Exception,e:
            exstr = traceback.format_exc()
            logger.critical("%s" % str(exstr))   
        
        return retCode,retData
    
    def keepAlive(self):
        ''''''
        return self.login()
    
    def sendReport(self):
        ''''''
        retCode=0
        retData=""
        sendData = ""

        rptNum = len(self.dectReportList)
        while rptNum is not 0:
            detRpt = self.dectReportList.pop()
            sendData += detRpt.pack()
            rptNum = len(self.dectReportList)
            
        if len(sendData) > 0:
            sendData = Packet.packHeader(sendData)
            logger.debug("send reports to %s..." % (Global.serverAddress) )
            retCode,retHeader,retData = self.report(Global.serverAddress,sendData)
            if retCode is 200:
                logger.info("send reports to %s ok" % (Global.serverAddress))
            else:
                logger.error("send reports to %s failed" % (Global.serverAddress))

        return retCode,retData
    
    def handleResponse(self,retdata):
        
        header={}
        ret = Packet.unpackHeader(retdata,header)
        if ret:
            taskDataList = Packet.unpackBody(header['valuelen'],header['value'])
            for taskData in taskDataList:
                if taskData['t'] == det_task_tag:
                    detTask = DetectTask()
                    detTask.unpack(taskData['l'],taskData['v'])
                    self.dectTaskList.append(detTask)
                    logger.info("get detect task id is %d" % int(detTask.id))

    def report(self,server,data):
        
        connected=False
        retCode=0
        retHeader=None
        retData = None
        
        comp = urlparse(server)
        conn = None
        try:
            headers = {'Connection':'Keep-Alive'}
            
            tmp=""
            if comp.port is not None:
                tmp = comp.hostname+':%d' % comp.port
            else:
                tmp = comp.hostname
            conn = httplib.HTTPConnection(tmp,timeout=10)
            conn.connect()
            connected = True
            conn.request(method="POST",url=comp.path,body=data,headers=headers)
           
            response = conn.getresponse()
            retCode = response.status    
            retHeader = response.getheaders()
            retData = response.read()
        except Exception,e:
            exstr = traceback.format_exc()
            logger.critical("%s" % str(exstr))   
        
        if connected and conn is not None:
            conn.close()
        
        return retCode,retHeader,retData
                
    def getDeviceInfo(self,info):
        '''
        '''
        hostname = socket.gethostname()
        
        iplist = socket.gethostbyaddr(hostname)

        #TODO: modify
        info['os'] = sys.platform
        info['mac'] = '00-22-FA-60-A4-5C'
        info['ip'] = iplist[2][0]
        info['mask'] = '255.255.255.0'
        info['gateway'] = '127.0.0.1'
        info['ldns'] = '127.0.0.1'
        info['app'] = Global.appVer
                
        
        
        
        
    
    
