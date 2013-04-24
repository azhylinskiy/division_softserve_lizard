#!/usr/bin/python2.7
from sys import stdin, stdout
from math import *

s = stdin.readline()
x = float(s)

yn = x
y = -1
while abs(yn - y) > 1e-5:
	y = yn
	yn = 0.5 * (y + x / y)
print "asqrt = ", yn
print "sqrt = ", sqrt(x)
