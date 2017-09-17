#!/usr/bin/env python

# 1.
print("Exercise 1")
ip = raw_input("Enter an IP:")
pos_dot1 = ip.find(".")
pos_dot2 = ip.find(".",pos_dot1+1)
pos_dot3 = ip.find(".",pos_dot2+1)

ip1 = int(ip[0:pos_dot1].strip("."))
ip2 = int(ip[pos_dot1:pos_dot2].strip("."))
ip3 = int(ip[pos_dot2:pos_dot3].strip("."))
ip4 = int(ip[pos_dot3:].strip("."))

if not ((ip1 >= 0 and ip1 <= 255) and (ip2 >= 0 and ip2 <= 255) and (ip3 >= 0 and ip3 <= 255) and (ip4 >= 0 and ip4 <= 255)):
	print("Not a valid address!")
elif (ip1 >= 0) and (ip1 < 128):
	print("Class A")
elif (ip1 >= 128) and (ip1 < 192):
	print("Class B")
elif (ip1 >= 192) and (ip1 < 224):
	print("Class C")
elif (ip1 >= 224) and (ip1 < 240):
	print("Class D")
elif (ip1 >= 240) and (ip1 < 256):
	print("Class E")
