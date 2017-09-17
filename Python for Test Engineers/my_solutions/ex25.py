#!/usr/bin/env python

import ex11 as Host
import unittest

host1 = Host.Host(ip = [8,8,8,8], hostname = "www.google.com", services = {"ftp": 22, "ssh": 10000})


class MyTest(unittest.TestCase):
	
	def testIp(self):
		host1 = Host.Host(ip = [8,8,8,8], hostname = "www.google.com", services = {"ftp": 22, "ssh": 10000})
		ip = [8,8,8,8]
		self.assertEqual(host1.ip,ip)

	def testHostname(self):
		host1 = Host.Host(ip = [8,8,8,8], hostname = "www.google.com", services = {"ftp": 22, "ssh": 10000})
		hostname = "www.google.com"
		self.assertEqual(host1.hostname,hostname)

unittest.main()