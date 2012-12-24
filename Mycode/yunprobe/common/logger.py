
import logging
import logging.handlers
import logging.config

class Logger:
    '''
    '''
    def __init__(self,logconf):
        logging.config.fileConfig(logconf)
        self.logger = logging.getLogger("main")
        """
        conf={}
        conf['name'] = 'main'
        conf['filename'] = logconf
        conf['format'] = "%(asctime)s-%(levelname)s-%(message)s" 
        conf["datefmt"]="%Y-%m-%d %H:%M:%S"
        self.logger = logging.getLogger(conf['name'])
        handler = logging.handlers.RotatingFileHandler(conf['filename'],
                                                       maxBytes=20,
                                                       backupCount=5)
        fmt = logging.Formatter(conf['format'],conf['datefmt'])
        handler.setFormatter(fmt)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
        """
        
    def debug(self,msg):
        self.logger.debug(msg)
    
    def info(self,msg):
        self.logger.info(msg)
    
    def warn(self,msg):
        self.logger.warn(msg)
    
    def error(self,msg):
        self.logger.error(msg)
    
    def critical(self,msg):
        self.logger.critical(msg)
        
    def log(self,level,msg):
        self.logger.log(level, msg)

if __name__ == '__main__':
    
    a = Logger("testlogging.conf")
    a.info("test")