#!/usr/bin/python2.7
from sys import stdin, stdout
from math import *

def sign(x):
	return copysign(1, x)

s = stdin.readline()
x = float(s)
s = 0 if sign(x - 2) == sign(x - 5) and sign(x - 1) == sign(x - -1) else 1
print s
