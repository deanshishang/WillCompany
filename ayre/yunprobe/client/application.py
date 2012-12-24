import sys, os, time, getopt, traceback
from client.global_ import *
from client.version import *
from client.dectwork import DectWork

class application:
	def __init__(self):
		self.option = {}
		self.option['mode'] = workMode['dect']
		#self.wgetUrl = ""

	def usage(self):
		print "WebProbe Client"
		print ""
		print "Usage: clientApp -s|--server serviceurl"
		print "		-s webprobe server address"
		print "		-v show version"
		print "		-h help"
		print ""

	def parseArguments(self, argv):
		try:
			Global.appPath = argv[0]
			opts, args = getopt.getopt(argv[1:], "hvs:", ["version", "help", "server="])
		except:
			self.usage()
			sys.exit(2)

		for o,a in opts:
			if o in ("-v", "--version"):
				print appVersion
				sys.exit()
			if o in ("-h", "--help"):
				self.usage()
				sys.exit()
			if o in ("-s", "--server"):
				if len(a) <= 0:
					self.usage()
					sys.exit(2)
				Global.serverAddress = a

		if len(Global.serverAddress) == 0:
			self.usage()
			sys.exit(2)

	def initialize(self):
		if self.option['mode'] is workMode['dect']:
			self.worker = DectWork()

	def run(self):
		try:
			if self.worker is not None:
				self.worker.process()
		except Exception, e:
			exstr = traceback.format_exc()
			logger.critical("%s" % exstr)
	def finalize(self):
		pass

app = application()

#if "__name__"=="__main__":
#	pass
