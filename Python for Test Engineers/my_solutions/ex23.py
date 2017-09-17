#!/usr/bin/env python

def areaDecorate(func):
	def funcWrapper(W, H, D=None):
		# print "In decorator"
		# print "W: {}".format(W)
		# print "H: {}".format(H)
		# print "D: {}".format(D)

		if W < 10 or W > 100:
			# raise ValueError('The width is not between 10 and 100')
			return('The width is not between 10 and 100')
		if H < 10 or H > 100:
			# raise ValueError('The height is not between 10 and 100')
			return('The height is not between 10 and 100')
		if D:
			if D < 10 or D > 100:
				# raise ValueError('The depth is not between 10 and 100')
				return('The depth is not between 10 and 100')
		return func(W, H, D)
	return funcWrapper

@areaDecorate
def calculateVolumeOrArea(W, H, D=None):
	# print "In calculate volume"
	# print "W: {}".format(W)
	# print "H: {}".format(H)
	# print "D: {}".format(D)

	if D:
		return W * H * D
	else:
		return W * H

print(calculateVolumeOrArea(30, 40))
print(calculateVolumeOrArea(30, 40, 20))
print(calculateVolumeOrArea(3, 4))
print(calculateVolumeOrArea(3, 4, 2))


def myDecorate(func):
	def funcWrapper(*arg,**kwarg):
		print("Added some really useful decoration!")
		return func(*arg,**kwarg)
	return funcWrapper

def myDecorateMore(func):
	def funcWrapper(*arg,**kwarg):
		print("Added some more really useful decoration!")
		return func(*arg,**kwarg)
	return funcWrapper


@myDecorate
@myDecorateMore
def mySimpleFunc(*arg,**kwarg):
	for a in arg:
		print a
	
	for a in kwarg:
		print a

mySimpleFunc("text1","text2",third_param="text3")

