#!/usr/bin/env python

from host import host as h
from host import hostmanager as hm

host1 = h.Host(ip = [8,8,8,8], hostname = "www.google.com", services = {"ftp": 22, "ssh": 10000})
host2 = h.Host(ip = [10,0,0,1], hostname = "www.mywebserver.com", services = {"http": 80, "ssh": 10000})

host1.printMembers()
host2.printMembers()

hostmanager = hm.HostManager(host1, host2)
hostmanager.listHostsWithService("ftp")
hostmanager.listHostsWithService("ssh")