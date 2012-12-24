#!/usr/bin/env python

from urlparse import urlparse
import httplib, urllib

from packet import *

'''
class Report:
    
        
    @classmethod
    def report(cls,server,data):
        
        connected=False
        retCode=0
        retHeader=None
        retData = None
        
        comp = urlparse(server)
        conn = None
        try:
            headers = {'Connection':'Keep-Alive'}
            connStr = "%s:%d" % (comp.hostname,comp.port) 
            conn = httplib.HTTPConnection(connStr,timeout=10)
            conn.connect()
            connected = True
            conn.request(method="POST",url=comp.path,body=data,headers=headers)
           
            response = conn.getresponse()
            retCode = response.status    
            retHeader = response.getheaders()
            retData = response.read()
        except:
            pass
        
        if connected and conn is not None:
            conn.close()
        
        return retCode,retHeader,retData
'''        

class LoginReport:
    
    "osversion + mac + ip + mask + gateway + ldns + appversion"
    
    def __init__(self):
        self.osver = ""
        self.ip = ""
        self.mac = ""
        self.mask = ""
        self.gateway = ""
        self.ldns = ""
        self.appver = ""
    
    def pack(self):
        pass
    
    def packWithHeader(self,info):
        '''
        '''
        osver = Tlv.pack(rpt_deviceosver_tag,info['os'])
        mac = Tlv.pack(rpt_devicemac_tag,info['mac'])
        ip = Tlv.pack(rpt_deviceip_tag,info['ip'])
        mask = Tlv.pack(rpt_devicemask_tag,info['mask'])
        gateway = Tlv.pack(rpt_devicegateway_tag,info['gateway'])
        ldns = Tlv.pack(rpt_deviceldns_tag,info['ldns'])
        appver = Tlv.pack(rpt_appver_tag,info['app'])
        
        ret = Tlv.pack(rpt_login_tag,osver+ip+mask+gateway+ldns+appver)
        return Packet.packHeader(ret)
        
    def unpack(self,datalen,data):
        ""
        read_len = 0
        while (datalen - read_len - Tlv.tagsize - Tlv.lensize) > 0:
            tlv_tag,tlv_len,tlv_value = Tlv.unpack(data[read_len:])
            if tlv_tag==rpt_deviceosver_tag:
                self.osver = tlv_value
            elif tlv_tag==rpt_devicemac_tag:
                self.mac = tlv_value
            elif tlv_tag==rpt_deviceip_tag:
                self.ip = tlv_value
            elif tlv_tag==rpt_devicemask_tag:
                self.mask = tlv_value
            elif tlv_tag==rpt_devicegateway_tag:
                self.gateway = tlv_value
            elif tlv_tag==rpt_deviceldns_tag:
                self.ldns = tlv_value
            elif tlv_tag==rpt_appver_tag:
                self.appver = tlv_value
                
            read_len += Tlv.tagsize + Tlv.lensize + int(tlv_len);
        
        
    
        
class DetectReport:
    ""
    def __init__(self,info=None):
        ''''''
        self.deviceId=0
        
        if info is not None:
            self.id = info['id']
            self.time = info['time']
            self.ip = info['urlip']
            self.t_dnslookup = info['t_dnslookup']
            self.t_connected = info['t_connected']
            self.t_firstbyte = info['t_firstbyte']
            self.t_download = info['t_download']
            self.l_object = info['l_object']
            self.httpCode = info['httpCode']
            self.retCode = info['retCode']
        
    def pack(self):
        
        ret = Tlv.pack(rpt_detectip_tag,self.ip)
        ret += Tlv.pack(rpt_detecttdnslookup_tag,str(self.t_dnslookup))
        ret += Tlv.pack(rpt_detecttconnected_tag,str(self.t_connected))
        ret += Tlv.pack(rpt_detecttfirstbyte_tag,str(self.t_firstbyte))
        ret += Tlv.pack(rpt_detecttdownload_tag,str(self.t_download))
        ret += Tlv.pack(rpt_detectlobject_tag,str(self.l_object))
        ret += Tlv.pack(rpt_detecthttpcode,str(self.httpCode))
        ret += Tlv.pack(rpt_detectretcode,str(self.retCode))
        ret += Tlv.pack(rpt_detecttime_tag,str(self.time))
        ret += Tlv.pack(rpt_detectid_tag,str(self.id))
        
        ret = Tlv.pack(rpt_detect_tag,ret)
        return ret
    
    def unpack(self,datalen,data):
        ''''''
        read_len = 0
        while (datalen - read_len - Tlv.tagsize - Tlv.lensize) > 0:
            tlv_tag,tlv_len,tlv_value = Tlv.unpack(data[read_len:])
            if tlv_tag==rpt_detecttime_tag:
                self.time = tlv_value
            elif tlv_tag==rpt_detectip_tag:
                self.ip = tlv_value
            elif tlv_tag==rpt_detecttdnslookup_tag:
                self.t_dnslookup = tlv_value
            elif tlv_tag==rpt_detecttconnected_tag:
                self.t_connected = tlv_value
            elif tlv_tag==rpt_detecttfirstbyte_tag:
                self.t_firstbyte = tlv_value
            elif tlv_tag==rpt_detecttdownload_tag:
                self.t_download = tlv_value
            elif tlv_tag==rpt_detectlobject_tag:
                self.l_object = tlv_value
            elif tlv_tag==rpt_detecthttpcode:
                self.httpCode = tlv_value
            elif tlv_tag==rpt_detectretcode:
                self.retCode = tlv_value
            elif tlv_tag==rpt_detectid_tag:
                self.id = tlv_value
                
            read_len += Tlv.tagsize + Tlv.lensize + int(tlv_len);
    

if __name__ == '__main__':
    
    #rpt = LoginReport()
    #data = rpt.packWithHeader()
    #print data
    ##prover,protype,devname,vallen,value = Packet.unpackHeader(data)
    ##retlist = Packet.unpackWrap(vallen,value)
    ##for item in retlist:
    ##    print item['t'],item['l'],item['v']
    ##    logRpt = LoginReport()
    ##    logRpt.unpack(item['l'],item['v'])
    ##    print logRpt.osver,logRpt.ip,logRpt.mask,logRpt.gateway,logRpt.ldns,logRpt.appver
    #rpt.report(data)
    
    rpt = Report();
    data = "1234567890"
    rpt.report(data);
    
    
    


    


