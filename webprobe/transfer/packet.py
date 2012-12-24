#!/usr/bin/env python

#import device
import socket

appVersion = '10001'
protocolVesion = '0001'
protocolType   = 'web1'


# define report tag list

rpt_login_tag =1
rpt_live_tag=2
rpt_detect_tag=3

rpt_devicename_tag=11
rpt_devicemac_tag=12
rpt_deviceip_tag=13
rpt_devicemask_tag=14
rpt_devicegateway_tag=15
rpt_deviceldns_tag=16
rpt_deviceosver_tag=17
rpt_appver_tag=18


rpt_detecttime_tag=19
rpt_detectip_tag=20
rpt_detecttdnslookup_tag=21
rpt_detecttconnected_tag=22
rpt_detecttfirstbyte_tag=23
rpt_detecttdownload_tag=24
rpt_detectlobject_tag=25
rpt_detecthttpcode=26
rpt_detectretcode=27

rpt_detectid_tag=30

#define detect tag list

det_task_tag = 1

det_id_tag=11
det_url_tag = 12
det_ip_tag = 13



class Tlv:
    '''tag   + len +    value
       4bytes  4bytes   
    '''
    
    tagsize = 4
    lensize = 4
    
    #TODO: check len
    
    @classmethod
    def pack(cls,tag,value):
        #if type(tag)==type(0) and type(value)==type(""):    
            ret = "%04d" % tag
            ret += "%04d" % len(value)
            ret += value
            return ret
        
    @classmethod
    def unpack(cls,tlv):
        if type(tlv)==type(""):
            t = tlv[0:cls.tagsize]
            l = tlv[cls.tagsize:(cls.tagsize+cls.lensize)]
            v = tlv[(cls.tagsize+cls.lensize):(cls.tagsize+cls.lensize+int(l))]
            return int(t),int(l),v
        
        


class Packet:
        
    lensize = 4
    
    @classmethod
    def packHeader(cls,value):
        '''
            version + type + tlv(devicename) + valuelen
        '''
        version = protocolVesion
        type = protocolType
        hostname = socket.gethostname()
        devname = Tlv.pack(rpt_devicename_tag,hostname)
        vallen = "%04d" % len(value)
        ret = version + type + devname + vallen + value
        return ret
    
    @classmethod
    def unpackHeader(cls,data,header):
        '''
        TODO: check MAC 
        '''
        
        verlen = len(protocolVesion)
        typelen = len(protocolType)
        
        if type(data) == type(""):
            if len(data) <= (verlen+typelen):
                return False
                
            verlen = len(protocolVesion)
            typelen = len(protocolType)
            header['prover'] = data[0:verlen]
            header['protype'] = data[verlen:(verlen+typelen)]
            if cmp(header['prover'],protocolVesion):
                return False
            if cmp(header['protype'],protocolType):
                return False
            
            remainData = data[verlen+typelen:]
            if len(remainData) <= (Tlv.tagsize + Tlv.lensize):
                return False
            tlv_tag,tlv_len,devicename = Tlv.unpack(remainData)
            header['devicename'] = devicename
            
            remainData = remainData[Tlv.tagsize+Tlv.lensize+int(tlv_len):]
            if len(remainData) <= cls.lensize:
                return False
            
            valuelen = int(remainData[0:cls.lensize])
            if valuelen <= (Tlv.tagsize + Tlv.lensize):
                return False
            value = remainData[cls.lensize:]
            header['valuelen'] = valuelen
            header['value'] = value
            
        return True

    @classmethod
    def unpackBody(cls,vlen,val):
        vlist=[]
        read_len = 0
        while (vlen - read_len - Tlv.tagsize - Tlv.lensize) > 0:
            tlv_tag,tlv_len,tlv_value = Tlv.unpack(val[read_len:])
            vlist.append({'t':int(tlv_tag),'l':int(tlv_len),'v':tlv_value})
            read_len += Tlv.tagsize + Tlv.lensize + int(tlv_len);
        
        return vlist
     