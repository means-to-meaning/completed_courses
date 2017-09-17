#!/usr/bin/env python

import os
import glob

cur_dir = os.getcwd()

dir_content = os.listdir(cur_dir)
for content in dir_content:
	print content


def createTestDir(dir_name):
	os.mkdir(dir_name)
	os.chdir(dir_name)
	f = open('testfile.txt','w')
	f.close()
	os.listdir(dir_name)

print("Running test dir first time")
dir_name = os.path.join('/Users/vlasp/src/amzn/feabhas_python/TestDirectory')
createTestDir(dir_name)

def addFiles(dir_name):
	os.chdir(dir_name)
	f = open('file1.txt','w')
	f.close()
	f = open('file2.txt','w')
	f.close()
	f = open('file3.py','w')
	f.close()
	f = open('file4.py','w')
	f.close()

print("Adding files to the dir")
dir_name = os.path.join('/Users/vlasp/src/amzn/feabhas_python/TestDirectory')
addFiles(dir_name)
print glob.glob(os.path.join(dir_name,'*.txt'))



print("Running test dir second time")
createTestDir('TestDirectory')

