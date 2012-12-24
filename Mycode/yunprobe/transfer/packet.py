import socket

#appVersion = 'erya2012'
protocolVersion = '0001'
protocolType = 'web1'

# define report tag list

rpt_login_tag = 1
rpt_live_tag = 2
rpt_detect_tag = 3

rpt_devicename_tag = 11
rpt_devicemac_tag = 12
rpt_deviceip_tag = 13
rpt_devicemask_tag = 14
rpt_devicegateway_tag = 15
rpt_deviceldns_tag = 16
rpt_deviceosver_tag = 17
rpt_appver_tag = 18

rpt_detecttime_tag = 19
rpt_detectip_tag = 20
rpt_detecttdnslookup_tag = 21
rpt_detecttconnected_tag = 22
rpt_detecttfirstbyte_tag = 23
rpt_detecttdownload_tag = 24
rpt_detectlobject_tag = 25
rpt_detecthttpcode = 26
rpt_detectretcode = 27

rpt_detectid_tag = 30
#define detect tag list

det_task_tag = 1
det_id_tag = 11
det_url_tag = 12
det_ip_tag = 13

class Tlv:
	'''
		tag    + len   + value
		4bytes   4bytes
	'''
	tagsize = 4
	lensize = 4

	#TODO: check len
	@classmethod
	def pack(self, tag, value):
		ret = "%04d" % tag
		ret += "%04d" % len(value)
		ret += value
		return ret

	@classmethod
	def unpack(self, tlv):
		if type(tlv) == type(""):
			t = tlv[0:self.tagsize]
			l = tlv[self.tagsize:(self.tagsize+self.lensize)]
			v = tlv[(self.tagsize+self.lensize):(self.tagsize+self.lensize+int(l))]
			return int(t), int(l), v

class Packet:
	lensize = 4

	@classmethod
	def packHeader(self, value):
		'''
			protocol_version + protocol_type + tlv(devicename) + valuelen + value
		'''
		version = protocolVersion
		ttype = protocolType
		hostname = socket.gethostname()
		devname = Tlv.pack(rpt_devicename_tag, hostname)
		vallen = "%04d" % len(value)
		ret = version + ttype + devname + vallen + value
		#print "ret:\n"
		#print ret
		return ret

	@classmethod
	def unpackHeader(self, data, header):
		verlen = len(protocolVersion)
		typelen = len(protocolType)

		if type(data) == type(""):
			if len(data) <= (verlen+typelen):
				return False

			verlen = len(protocolVersion)
			typelen = len(protocolType)
			header['prover'] = data[0:verlen]
			header['protype'] = data[verlen:(verlen+typelen)]
			if cmp(header['prover'], protocolVersion):
				return False
			if cmp(header['protype'], protocolType):
				return False


			remainData = data[verlen+typelen:]
			if len(remainData) <= (Tlv.tagsize + Tlv.lensize):
				return False

			#print remainData
			tlv_tag, tlv_len, devicename = Tlv.unpack(remainData)
			header['devicename'] = devicename
	
	
			remainData = remainData[Tlv.tagsize+Tlv.lensize+int(tlv_len):]
			if len(remainData) <= self.lensize:
				return False
	
			valuelen = int(remainData[0:self.lensize])
			if valuelen <= (Tlv.tagsize + Tlv.lensize):
				return False
			value = remainData[self.lensize:]
			header['valuelen'] = valuelen
			header['value'] = value
	
		return True

	@classmethod
	def unpackBody(self, vlen, val):
		vlist = []
		read_len = 0
		while(vlen - read_len - Tlv.tagsize - Tlv.lensize) > 0:
			tlv_tag, tlv_len, tlv_value = Tlv.unpack(val[read_len:])
			vlist.append({'t':int(tlv_tag),'l':int(tlv_len), 'v':tlv_value})
			read_len += Tlv.tagsize + Tlv.lensize + int(tlv_len);

		return vlist
