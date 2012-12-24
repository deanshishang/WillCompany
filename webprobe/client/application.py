
import sys, os, time,getopt,traceback

from client.version import *
from client.global_ import *
from client.dectwork import DectWork
from client.wgetwork import WgetWork
  
class daemonizeError(Exception): pass

class application:
    '''
    '''
    def __init__(self):
        self.option = {}
        self.option['daemon'] = False
        self.option['mode'] = workMode['dect']
        self.wgetUrl=""
    
    def usage(self):
        print "WebProbe Client"
        print ""
        print "Usage: clientApp -s|--server serviceurl [-w|--wget url]"
        print "       -s webprobe server address"
        print "       -d daemon,only support linux "
        print "       -w wget the url"
        print "       -v show version"
        print ""
            
    def parseArguments(self,argv):
        try:
            Global.appPath = argv[0]
            opts,args = getopt.getopt(argv[1:],"dhw:vs:",["version","daemon","help","wget","server"])
        except:
            self.usage()
            sys.exit(2)
        
        for o,a in opts:
            
            if o in("-v","--version"):
                print app_version
                sys.exit()
            if o in("-h","--help"):
                self.usage()
                sys.exit()
            if o in("-d","--daemon"):
                self.option['daemon'] = True
                
            if o in("-w","--wget"):
                if len(a) <=0:
                    self.usage()
                    sys.exit(2)
                self.wgetUrl = a
                self.option['mode'] = workMode['wget']
            
            if o in("-s","--server"):
                if len(a) <=0:
                    self.usage()
                    sys.exit(2)
                Global.serverAddress = a

        if len(self.wgetUrl)==0 and len(Global.serverAddress)==0:
            self.usage()
            sys.exit(2)
        
    
    def initialize(self):
        """
        """
        if self.option['mode'] is workMode['wget']:
            self.worker = WgetWork(self.wgetUrl)
        elif self.option['mode'] is workMode['dect']:
            if self.option['daemon']:
                self.daemonize()
            self.worker = DectWork()
        
    def run(self):
        """
        """
        try:
            if self.worker is not None:
                self.worker.process()
        except Exception,e:
            exstr = traceback.format_exc()
            logger.critical("%s" % str(exstr))   
    
    def finalize(self):
        pass

    def daemonize(self):  
         '''
         '''
         if cmp(sys.platform,"win32"):
             
             from signal import SIGINT,SIGTERM,SIGKILL
             # flush io  
             sys.stdout.flush()  
             sys.stderr.flush()  
           
             # Do first fork.  
             try:   
                 pid = os.fork()   
                 if pid > 0: sys.exit(0) # Exit first parent.  
             except OSError, e:   
                 sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))  
                 sys.exit(1)  
                   
             # Decouple from parent environment.  
             os.chdir("/")   
             os.umask(0)   
             os.setsid()   
               
             # Do second fork.  
             try:   
                 pid = os.fork()   
                 if pid > 0: sys.exit(0) # Exit second parent.  
             except OSError, e:   
                 sys.stderr.write("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror))  
                 sys.exit(1)  
                 
             # Open file descriptors and print start message  
             #si = file(self.stdin, 'r')  
             #so = file(self.stdout, 'a+')   
             #se = file(self.stderr, 'a+', 0)  #unbuffered  
             #pid = str(os.getpid())  
             #sys.stderr.write("\n%s\n" % startmsg % pid)  
             #sys.stderr.flush()  
             #if pidfile: file(pidfile,'w+').write("%s\n" % pid)  
               
             # Redirect standard file descriptors.  
             #os.dup2(si.fileno(), sys.stdin.fileno())  
             #os.dup2(so.fileno(), sys.stdout.fileno())  
             #os.dup2(se.fileno(), sys.stderr.fileno())  
   
    """
    def startstop(self,action=None ):  
                     
         if not action and len(sys.argv) > 1:  
             action = sys.argv[1]  
       
         if action:  
             try:  
                 pf  = file(pidfile,'r')  
                 pid = int(pf.read().strip())  
                 pf.close()  
             except IOError: 
                 pid = None  
             if 'stop' == action or 'restart' == action:  
                 if not pid:  
                     mess = "Could not stop, pid file '%s' missing.\n"  
                     raise daemonizeError(mess % pidfile)  
                 try:  
                    while 1:  
                        print "sending SIGINT to",pid  
                        os.kill(pid,SIGINT)  
                        time.sleep(2)  
                        print "sending SIGTERM to",pid  
                        os.kill(pid,SIGTERM)  
                        time.sleep(2)  
                        print "sending SIGKILL to",pid  
                        os.kill(pid,SIGKILL)  
                        time.sleep(1)  
                 except OSError, err:  
                    print "process has been terminated."  
                    os.remove(pidfile)  
                    if 'stop' == action:  
                        return    ## sys.exit(0)  
                    action = 'start'  
                    pid = None  
             if 'start' == action:  
                 if pid:  
                     mess = "Start aborted since pid file '%s' exists. Server still running?\n"  
                     raise daemonizeError(mess % pidfile)  
                 daemonize()  
                 return  
         print "usage: %s start|stop|restart" % sys.argv[0]  
         raise daemonizeError("invalid command")  
     """ 
     
app = application()
   
if __name__ == "__main__":  
     pass



