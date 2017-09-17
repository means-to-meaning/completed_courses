#!/usr/bin/env python

import sys

ERR_FILE_NOT_EXIST = 1

filename = "filedoesnotexist.txt"

try:
	fh = open(filename, 'r')
	for line in f.readlines():
		print line
	f.close()
except IOError as e:
	print("Found an exception: " + str(e))
