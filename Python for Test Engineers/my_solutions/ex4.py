#!/usr/bin/env python

# 1.
print("Exercise 1")
print("1/2")
print(1/2)
print("1.0/2")
print(1.0/2)
print("float(1)/2")
print(float(1)/2)

# 2.
print("Exercise 2")
bits = 1024 * 8
print(bits)
combinations = 2 ** bits
print(combinations)

combinations2 = 2 ** long(bits)
print(combinations2)

# 3.
print("Exercise 3")
def calcHypoteneuse(a,b):
	return (a ** 2 + b ** 2) ** 0.5
print(calcHypoteneuse(3,4))