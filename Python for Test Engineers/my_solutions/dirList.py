#!/usr/bin/env python

import os
import glob
import sys

def readDirNames():
	for dir_name in sys.stdin.readlines():
		dir_name = dir_name[:-1]
		print(os.listdir(dir_name))

readDirNames()