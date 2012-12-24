

from common.logger import Logger

logger = Logger("etc/clientlogging.conf")


workMode = {'dect':0,
            'wget':1,
           }

class Global:
    
    appPath = ""
    appVer = "10001"
    serverAddress = ""
    keepAliveInterval = 60
    sendReportInterval = 30