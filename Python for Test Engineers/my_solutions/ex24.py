#!/usr/bin/env python

import threading
import os

n_files = 0
lock = threading.Lock()
global_stop = False

class ThreadedClass(threading.Thread):

	def __init__(self,path):
		threading.Thread.__init__(self)
		self.path = path

	def run(self):
		print("Starting dir parsing thread")
		global n_files
		global global_stop
		for dir, dirs, files in os.walk(self.path):
			if not global_stop:
				lock.acquire()
				try:
					n_files += len(files)
				finally:
					lock.release()
			else:
				break
		print("Exiting thread run")
		print(n_files)


count_thread = ThreadedClass('/')
count_thread.start()

while True:
	input = raw_input("Press any key for update or \'q\' to terminate!")
	if input == 'q':
		print "Received a terminate signal from user"
		global_stop = True
		print global_stop
		break
	lock.acquire()
	print "Files so far: {}".format(n_files)
	lock.release()

count_thread.join()