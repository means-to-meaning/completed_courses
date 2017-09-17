#!/usr/bin/env python

def formatIp(ipList):
	return str(ipList[0]) + "." + str(ipList[1]) + "." + str(ipList[2]) + "." + str(ipList[3])

class HostManager():

	def __init__(self, *arg):
		self.hosts = arg

	def listHostsWithService(self, service):
		for host in self.hosts:
			if service in host.services:
				print "Host ip: %s, Hostname: %s, Service: %s, Port %d" % (formatIp(host.ip), host.hostname, service, host.services.get(service))
