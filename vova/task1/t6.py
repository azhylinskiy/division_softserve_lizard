#!/usr/bin/python2.7
from sys import stdin, stdout
from math import *

def sign(x):
	return copysign(1, x)

s = stdin.readline()
arr = [int(x) for x in s.split()]

s = 0
for i in range(len(arr) - 1):
	if (sign(arr[i]) != sign(arr[i + 1])):
		s = s + 1
print "alternatings: ", s
print "signt 3, 0, -5: ", sign(3), sign(0), sign(-5)
