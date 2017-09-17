#!/usr/bin/env python

class Complex:

	def __init__(self,a=0,b=0):
		self.a = float(a)
		self.b = float(b)

	def __str__(self):
		if self.a >= 0:
			str_rep_a = "{0:.2f}".format(self.a)

		elif self.a < 0:
			str_rep_a = "{0:.2f}".format(self.a)
		else:
			raise Exception("Cannot handle this value of a: " + str(self.a))

		if self.b >= 0:
			str_rep_b = "+{0:.2f}i".format(self.b)
		elif self.b < 0:
			str_rep_b = "{0:.2f}i".format(self.b)
		else:
			raise Exception("Cannot handle this value of b: " + str(self.b))

		return str_rep_a + str_rep_b


	def __add__(self,y):
		return Complex(self.a + y.a, self.b + y.b)

	def __sub__(self,y):
		return Complex(self.a - y.a, self.b - y.b)

	def __mul__(self,y):
		return Complex(self.a * y.a - self.b * y.b, self.b * y.a + self.a * y.b)

	def __div__(self,y):
		assert self.b != 0 or y.b != 0, "Division not possible: Both c and d are 0!"
		re = (self.a * y.a + self.b * y.b) / (y.a ** 2 + y.b ** 2)
		im = (self.b * y.a - self.a * y.b) / (y.a ** 2 + y.b ** 2)
		return Complex(re, im)

	def mod(self):
		return Complex((self.a ** 2 + self.b ** 2) ** 0.5,0)

c = raw_input().split(" ")
d = raw_input().split(" ")

c2 = Complex(float(c[0]),float(c[1]))
c3 = Complex(float(d[0]),float(d[1]))


print(c2 + c3)
print(c2 - c3)
print(c2 * c3)
print(c2 / c3)
print(c2.mod())
print(c3.mod())