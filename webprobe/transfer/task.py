

from packet import *


class DetectTask:
    
    def __init__(self,id='',url='',ip=''):
        self.id = id
        self.url = url
        self.ip = ip

    def pack(self):
        ''''''
        id = Tlv.pack(det_id_tag,str(self.id))
        url = Tlv.pack(det_url_tag,self.url)
        ip = Tlv.pack(det_ip_tag,self.ip)
        return id+url+ip
    
    def unpack(self,datalen,data):
        #TODO: check len
        read_len = 0
        while (datalen - read_len - Tlv.tagsize - Tlv.lensize) > 0:
            tlv_tag,tlv_len,tlv_value = Tlv.unpack(data[read_len:])
            if tlv_tag==det_url_tag:
                self.url = tlv_value
            elif tlv_tag==det_ip_tag:
                self.ip = tlv_value
            elif tlv_tag==det_id_tag:
                self.id = tlv_value
                
            read_len += Tlv.tagsize + Tlv.lensize + int(tlv_len);
    
    