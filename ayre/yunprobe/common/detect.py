#!/usr/bin/env python

from urlparse import urlparse
import socket,httplib,time,sys

class HttpDetect:
    ""
    def __init__(self):
        
        self.httpCode=0
        self._iserror = None
        self._retCode = 0
        self._retMsg = "OK"
        self._urlip = ""
        self.t_dnslookup = 0
        self.t_connected = 0
        self.t_firstbyte = 0
        self.t_download = 0
        self.l_object = 0
    
    def do(self,url):
       
        #comps = urlparse(url)
        #for Python 2.3
        comp = urlparse(url)
        class Comps:
            pass
        comps = Comps
        comps.hostname = comp[1]
        comps.port = 80
        comps.path = comp[2]

        headers = {'Host':comps.hostname,
                   'Connection':'Keep-Alive',}

        #parse
        if self._iserror is None:
            begintime =  time.time()
            try:
                addr = socket.getaddrinfo(comps.hostname,comps.port)
                self._urlip = addr[0][4][0]
            except Exception ,e:
                print 'parse failed'
                self._iserror = True
                self._retCode = e[0]
                #self._retMsg = e[1]
            parseendtime = time.time()
            self.t_dnslookup = parseendtime - begintime
        
        #connected
        if self._iserror is None:
            try:
                if comps.port is not None:
                    tmp = self._urlip+':%d' % comps.port
                else:
                    tmp = self._urlip
                conn = httplib.HTTPConnection(tmp)
                conn.connect()
            except Exception,e:
                print 'connected failed'
                self._iserror = True
                self._retCode = e[0]
                #self._retMsg = e[1]
            connectedtime = time.time()
            self.t_connected = connectedtime - parseendtime
        
        #first byte
        if self._iserror is None:
            try:
                conn.request(method="GET",url=comps.path,headers=headers)
                response = conn.getresponse()
                self.httpCode = response.status
            except Exception,e:
                print 'first byte failed'
                self._iserror = True
                self._retCode = e[0]
                #self._retMsg = e[1]
            resptime = time.time()
            self.t_firstbyte = resptime-connectedtime
        
        #download
        if self._iserror is None:
            try:
                self.l_object = len(response.read())
            except Exception,e:
                print 'download failed'
                self._iserror = True
                self._retCode = e[0]
                #self._retMsg = e[1]
            downloadedtime = time.time()
            self.t_download = downloadedtime - resptime
        
        dict={}
        dict['time'] = int(time.time())
        dict['urlip'] = self._urlip
        dict['t_dnslookup'] = int(self.t_dnslookup*1000)
        dict['t_connected'] = int(self.t_connected*1000)
        dict['t_firstbyte'] = int(self.t_firstbyte*1000)
        dict['t_download'] = int(self.t_download*1000)
        dict['l_object'] = int(self.l_object)
        dict['httpCode'] = self.httpCode
        dict['retCode'] = self._retCode

        return dict
    
    
if __name__ == '__main__':
    
    if sys.argv[1] is not None:
        det = Detect();
        #det.do("http://download.rising.com.cn:80/do_not_delete/noc.gif ")
        print det.do(sys.argv[1])
    
    
