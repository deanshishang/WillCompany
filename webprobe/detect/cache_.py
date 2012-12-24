
import time,traceback

from django.db import connection

from global_ import logger
from transfer.task import *
import models


class CacheDb:
    '''
    '''
    device={}
    
    @staticmethod
    def syncAllFromDb():
        #TODO:  lock
        
        try:
            deviceList=[]
            cursor = connection.cursor()
            sql = "select name,id from detect_device"
            cursor.execute(sql)
            row = cursor.fetchone()
            while row:
                device={}    
                device['name'] = row[0]
                device['id'] = row[1]
                deviceList.append(device)
                CacheDb.device[row[0]]={'id':row[1]}
                row = cursor.fetchone()
            
            for device in deviceList:
            
                deviceName = device['name']
                deviceId = device['id']
                sql = "select t.id,t.url,t.ip,t.interval from detect_task t, detect_device_tasks r " \
                      "where t.id=r.task_id and r.device_id=%d" % deviceId
                cursor.execute(sql)
                row = cursor.fetchone()
                while row:
                    taskId = row[0]
                    detectUrl = row[1]
                    detectIp = row[2]
                    detectInterval = row[3]
                    if CacheDb.device.has_key(deviceName):
                        if CacheDb.device[deviceName].has_key('task'):
                            CacheDb.device[deviceName]['task'][taskId] = {'url':detectUrl,
                                                                          'ip':detectIp,
                                                                          'interval':detectInterval,
                                                                          'lasttime':int(time.time()),
                                                                          'detectNum':0}
                        else:
                           CacheDb.device[deviceName]['task'] ={taskId:{'url':detectUrl,
                                                                        'ip':detectIp,
                                                                        'interval':detectInterval,
                                                                        'lasttime':int(time.time()),
                                                                        'detectNum':0}} 
                
                    row = cursor.fetchone()
        except Exception,e:
            exstr = traceback.format_exc()
            logger.critical("%s" % str(exstr))
                
    @staticmethod            
    def updateAndGetTaskList(deviceName,detRpt,taskList):
        #TODO: lock
        result = False
        if CacheDb.device.has_key(deviceName):
            
            detRpt.deviceId = CacheDb.device[deviceName]['id']
            taskDict = {}
            if CacheDb.device[deviceName].has_key('task'):
                taskDict= CacheDb.device[deviceName]['task']
            
            #update
            if taskDict.has_key(int(detRpt.id)):
                info = taskDict[int(detRpt.id)]
                info['detectNum'] += 1
                info['lasttime'] = int(time.time())
                result = True
            #get task list   
            CacheDb.getTaskList(deviceName,taskList)
                
        return result
    
    @staticmethod            
    def getTaskList(deviceName,taskList):
        #TODO: lock
        result = False
        if CacheDb.device.has_key(deviceName):
            
            result = True
            taskDict={}
            if CacheDb.device[deviceName].has_key('task'):
                taskDict = CacheDb.device[deviceName]['task']
            #get task list
            for key in taskDict.keys():
                #check time
                info = taskDict[key]
                interval = info['interval'] *60  # to second
                curtime = int(time.time())
                if (info['lasttime'] + interval) < curtime:
                    logger.debug("last:%d + interval:%d < curtime:%d" %(info['lasttime'],interval,curtime))
                    task = DetectTask(key,info['url'],info['ip'])
                    taskList.append(task)
                else:
                    logger.debug("last:%d + interval:%d >= curtime:%d" % (info['lasttime'],interval,curtime))
                
                
        return result
        
        

CacheDb.syncAllFromDb()

