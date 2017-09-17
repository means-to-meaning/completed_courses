#!/usr/bin/env python
import sys

# 1.
print("Exercise 1")
ip = raw_input("Enter an IP:")

ip_list = ip.split(".")
print(ip_list)

ip_ranges = [
			range(0,128),
			range(128,192),
			range(192,223),
			range(224,239),
			range(240,255)
			]
print(ip_ranges[0])
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


#3
print ("Exercise 3")
years =  [""] * 3000
months = [""] * 13
days = [""] * 32

for month in range(1,14):
	months[month-1] = days


for year in range(1,3001):
	years[year-1] = months

print(len(years))
print(len(months))
print(len(days))
print(len(date),len(date[1]))

sys.getsizeof(date)

# date[2016][12][31] = "remind me about the dentist"
# date[2016][12][31]

years =  [None] * 3000
months = [None] * 13
days = [None] * 32

for month in range(1,14):
	months[month-1] = days


for year in range(1,3001):
	years[year-1] = months

print(len(years))
print(len(months))
print(len(days))
print(len(date),len(date[1]))

sys.getsizeof(date)

