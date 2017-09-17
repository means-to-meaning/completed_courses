#!/usr/bin/env python

def isInternalIp(address):
	ip_list = address.split(".")

	if (int(ip_list[0]) == 192) and (int(ip_list[1]) == 168):
		return True
	else:
		return False

print(isInternalIp("192.168.0.1"))
print(isInternalIp("10.0.0.1"))

def getInternalIps():
	quad3 = range(0,256)
	quad4 = range(0,256)

	ips = []
	a = 192
	b = 168
	for c in quad3:
		for d in quad4:
			ip = ".".join([str(a),str(b),str(c),str(d)])
			ips.append(ip)
	return ips

ips = getInternalIps()
print(ips[:10])
print(ips[-10:])


def calculateVolumeOrArea(W, H, D=None):
	if D:
		return W * H * D
	else:
		return W * H

print(calculateVolumeOrArea(3, 4))
print(calculateVolumeOrArea(3, 4, 2))

iter = 0
def quicksort(array):
	global iter
	iter += 1
	if (len(array)) <= 1:
		return array
	ind_pivot = int(round(len(array)/2))
	pivot_elem = array.pop(ind_pivot)
	less = []
	greater = []
	for elem in array:
		if elem <= pivot_elem:
			less.append(elem)
		else:
			greater.append(elem)

	print("Iteration: %d" % iter)
	print less
	print pivot_elem
	print greater
	return(quicksort(less) + [pivot_elem] + quicksort(greater))

a = [3,4,1,5,6]
print(a)
res = quicksort(a)
print(res)

a = [1,1,2]
print(a)
print(quicksort(a))

a = []
print(a)
print(quicksort(a))

a = [0]
print(a)
print(quicksort(a))