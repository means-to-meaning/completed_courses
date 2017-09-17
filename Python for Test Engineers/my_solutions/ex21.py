#!/usr/bin/env python

import subprocess
import threading

class CmdExecutor:
	
	ERR_SUBPROCESS = 1

	@staticmethod
	def termProc(proc):
		print "Force terminating the process!"
		proc.terminate()

	def __init__(self,cmd,timeout=None):
		self.cmd = cmd
		self.return_code = None
		self.return_stdout = None
		self.return_stderr = None

	def execCmd(self,timeout=None):
		print("Executing command: \n" + " ".join(cmd))
		try:
			if not timeout:
				print("Executing command without timeout")
				proc = subprocess.Popen(self.cmd,bufsize=-1,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			if timeout > 0:
				print("Executing command with timeout")
				proc = subprocess.Popen(self.cmd,bufsize=-1,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				t = threading.Timer(timeout,CmdExecutor.termProc,[proc])
				t.start()
		except Exception as e:
			return(CmdExecutor.ERR_SUBPROCESS,"","Caught an exception while executing the cmd: {}\n{}".format(" ".join(self.cmd),e.message))
		proc.wait()
		self.return_stdout = " ".join(proc.stdout.readlines())
		self.return_stderr = " ".join(proc.stderr.readlines())
		proc.communicate()
		self.return_code = proc.returncode

	def __str__(self):
		return "Return code: {}\nStdout:\n{}Stderr:\n{}".format(self.return_code,self.return_stdout,self.return_stderr)


cmd = ['ls', '-al']
exec_cmd = CmdExecutor(cmd)
exec_cmd.execCmd()
print(exec_cmd)

cmd = ['cat', 'file1.txt']
exec_cmd = CmdExecutor(cmd)
exec_cmd.execCmd()
print(exec_cmd)

cmd = ['sh','sleepScript.sh', '5']
exec_cmd = CmdExecutor(cmd)
exec_cmd.execCmd(2)
print(exec_cmd)

