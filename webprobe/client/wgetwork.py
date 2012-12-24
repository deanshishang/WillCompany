'''
'''

from common.detect import *

class WgetWork:
    '''
    '''
    def __init__(self,url):
        self.url = url
    
    def process(self):
        
        detect = HttpDetect()
        dict = detect.do(self.url)
        print self.url,dict['urlip'],dict['t_dnslookup'],dict['t_connected'],dict['t_firstbyte'],dict['t_download'],dict['l_object'],dict['httpCode'],
        
