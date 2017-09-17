#!/usr/bin/env python

class Host(object):

	def __init__(self, ip = [], hostname = "", services = {}):
		self.ip = ip
		self.hostname = hostname
		self.services = services

	def getIp(self):
		return self.ip

	def setIp(self,ip):
		self.ip = ip

	def getHostname(self):
		return self.hostname

	def setHostname(self,hostname):
		self.hostname = hostname

	def hasService(self,service):
		return service in self.services

	def addService(self, service, port):
		self.services[service] = port

	def printMembers(obj, type="Attributes"):
		members = dir(obj)
		mem_list = []
		for member in members:
			if (type == "Attributes") and (not callable(getattr(obj,member))):
				mem_list.append(member)
			if (type == "Methods") and (not callable(getattr(obj,member))):
				mem_list.append(member)
		print mem_list

def main():
	host1 = Host(ip = [8,8,8,8], hostname = "www.google.com", services = {"ftp": 22, "ssh": 10000})
	host2 = Host(ip = [10,0,0,1], hostname = "www.mywebserver.com", services = {"http": 80, "ssh": 10000})

	host1.printMembers()
	host2.printMembers()

if __name__ == "__main__":
	main()