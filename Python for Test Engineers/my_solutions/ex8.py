#!/usr/bin/env python
import sys

# 1.
print("Exercise 1")
ips = []

while True:
	ip = raw_input("Enter an IP. (To exit type \'q\'):")
	if ip == 'q':
		break
	ips.append(ip)
print(ips)

for ip in ips:
	ip_list = ip.split(".")
	print(ip_list)

	ip_ranges = [
				range(0,128),
				range(128,192),
				range(192,223),
				range(224,239),
				range(240,255)
				]
	if int(ip_list[0]) in ip_ranges[0]:
		print ("IP in class A")
	elif int(ip_list[0]) in ip_ranges[1]:
		print ("IP in class B")
	elif int(ip_list[0]) in ip_ranges[2]:
		print ("IP in class C")
	elif int(ip_list[0]) in ip_ranges[3]:
		print ("IP in class D")
	elif int(ip_list[0]) in ip_ranges[4]:
		print ("IP in class E")
	else:
		print ("IP not recognized")

# 2.
print("Exercise 2")

res = []
fn_str = "01-result.xls,2-result.xls,03-result.xls,05-result.xls"
fn_list = fn_str.split(',')

for fn in fn_list:
	temp = fn.split(".")
	temp = temp[0].split("-")
	res.append(temp[1] + str(int(temp[0])))

print(res)

# 3.
print("Exercise 3")
max_value = raw_input("Enter an number:")
for num in range(int(max_value)):
	if(num % 2 == 0):
		print(str(num) + " is even")
	if(num % 2 == 1):
		print(str(num) + " is odd")

