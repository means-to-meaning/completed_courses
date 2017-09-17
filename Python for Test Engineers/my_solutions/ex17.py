#!/usr/bin/env python

import socket, select, string, sys

host = sys.argv[1]
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)

try:
	s.connect((host,port))
	print("Connected to remote host {}".format(host))
except:
	print("Unable to connect")
	sys.exit()
else:
	try:
		msg = 'GET / HTTP/1.1\r\nHost: www.chess.co.uk\r\nConnection: close\r\n\r\n'
		s.sendall(msg)
	except Exception as e:
		print str(e)
		sys.exit()
	else:
		reply = "1"
		data = ""
		while (not reply == ""):
			"Reading new socket buffer"
			reply = s.recv(4096)
			"Adding buffer to receive data"
			data += reply
			# if reply == '' or (not reply):
			# 	s.close()
			# 	sys.exit()
			print reply
		s.close()

# try:
# 	s.connect((host,port))
# except:
# 	print("Unable to connect")
# 	sys.exit()
# print("Connected to remote host {}".format(host))
# while True:
# 	socket_list = [sys.stdin, s]
# 	read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
# 	for sock in read_sockets:
# 		if sock == s:
# 			data = sock.recv(4096)
# 			if not data:
# 				print('Connection closed')
# 				sys.exit()
# 			else:
# 				sys.stdout.write(data)
# 		# user entered a message
# 		else:
# 			msg = sys.stdin.readline()
# 			print msg
# 			s.send(msg)

