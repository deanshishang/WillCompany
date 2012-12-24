

from django.db import connection
from transfer.packet import *
from transfer.report import *
from transfer.task import *
import models
from cache_ import *

'''
    sync: http://127.0.0.1:8000/detect/sync  
'''

class Handler:
    
    @classmethod
    def handle(cls,deviceName,reportDataList):
        ''''''
        taskList=[]
        for reportData in reportDataList:
            if reportData['t'] == rpt_login_tag:
                lgnRpt = LoginReport()
                lgnRpt.unpack(reportData['l'],reportData['v'])
                taskList = cls.handleLogin(deviceName,lgnRpt)
            elif reportData['t'] == rpt_detect_tag:
                detRpt = DetectReport()
                detRpt.unpack(reportData['l'],reportData['v'])
                taskList = cls.handleDetect(deviceName,detRpt)
            else:
                return "NOT SUPPORT"
        
        retData = ""
        for task in taskList:
            data = task.pack()
            retData += Tlv.pack(det_task_tag,data)
            
        return Packet.packHeader(retData)
                
    @classmethod
    def handleLogin(cls,deviceName,lgnRpt):
        ''''''
        taskList =[]
        lgnHandler = LoginHandler()
        if not CacheDb.getTaskList(deviceName,taskList):
            lgnHandler.insertDbDevice(deviceName,lgnRpt)
        
        lgnHandler.insertDbDeviceStatus(deviceName, lgnRpt)
        
        return taskList
    
    @classmethod
    def handleDetect(cls,deviceName,detRpt):
        taskList =[]
        detHandler = DetectHandler()
        if CacheDb.updateAndGetTaskList(deviceName,detRpt,taskList):
            detHandler.insertDbDtData(deviceName,detRpt)
        return taskList
    
    
    @classmethod
    def queryFromDb(cls,deviceName,taskDataList):
        #TODO: from cache
             
        #from db
        deviceExist = False
        deviceId = None
        
        #query db device
        cursor = connection.cursor()
        sql = "select * from detect_device where name='%s'" % str(deviceName)
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            deviceId = int(row[0])
            deviceExist = True
            break
        
        if deviceId:
            #query task
            sql = "select t.url,t.ip from detect_task t, detect_device_tasks r " \
                  "where t.id=r.task_id and r.device_id=%d" % deviceId
            cursor.execute(sql)
            row = cursor.fetchone()
            while row:
                task = DetectTask(row[0],row[1])
                data = task.pack()
                taskDataList.append(data)
                row = cursor.fetchone()
        
        cursor.close()
        
        return deviceExist
            

class LoginHandler:
    
    def __init__(self):
        pass
    
    def handle(self):
        '''
        '''
        pass  
    
    def insertDbDevice(self,deviceName,lgnRpt):
        ''''''
        device = models.Device(name=deviceName)
        device.save()
    
    def insertDbDeviceStatus(self,deviceName,lgnRpt):
        ''''''
        deviceStatus = models.DeviceStatus(device_name=deviceName,
                                           mac_address=lgnRpt.mac,
                                           ip=lgnRpt.ip,
                                           mask=lgnRpt.mask,
                                           gateway=lgnRpt.gateway,
                                           ldns=lgnRpt.ldns,
                                           os_version=lgnRpt.osver,
                                           app_version=lgnRpt.appver)
        deviceStatus.save()
        
    
class DetectHandler:
    
    def __init__(self):
        pass
    
    def handle(self):
        pass
    
    def insertDbDtData(self,deviceName,detRpt):
        
        detectData = models.DtData(task_id=detRpt.id,
                                    device_id=detRpt.deviceId,
                                    dttime=detRpt.time,
                                    t_dnslookup=detRpt.t_dnslookup,
                                    ip_conn=detRpt.ip,
                                    t_conned = detRpt.t_connected,
                                    t_firstbyte=detRpt.t_firstbyte,
                                    t_download=detRpt.t_download,
                                    l_object=detRpt.l_object,
                                    http_code=detRpt.httpCode,
                                    result_code=detRpt.retCode)
                                   
        detectData.save() 

            