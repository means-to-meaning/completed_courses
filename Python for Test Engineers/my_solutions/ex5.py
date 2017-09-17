#!/usr/bin/env python

# 1.
print("Exercise 1")
ip = raw_input("Enter an IP:")
pos_dot1 = ip.find(".")
pos_dot2 = ip.find(".",pos_dot1+1)
pos_dot3 = ip.find(".",pos_dot2+1)
#print(pos_dot1,pos_dot2,pos_dot3)
print(ip[0:pos_dot1] + " " + ip[pos_dot1:pos_dot2] + " " + ip[pos_dot2:pos_dot3] +" " + ip[pos_dot3:])


print("Exercise 2")
print(ip[0:pos_dot1] + " " + ip[pos_dot1+1:pos_dot2] + " " + ip[pos_dot2+1:pos_dot3] +" " + ip[pos_dot3+1:])
print(int(ip[0:pos_dot1].strip(".")), int(ip[pos_dot1:pos_dot2].strip(".")), int(ip[pos_dot2:pos_dot3].strip(".")), int(ip[pos_dot3:].strip(".")))
