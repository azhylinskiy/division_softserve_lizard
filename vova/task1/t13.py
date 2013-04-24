#!/usr/bin/python2.7
from sys import stdin, stdout
from math import *

s = stdin.readline()
x = float(s)

if x <= 0.5:
	print sin(pi / 2)
else:
	print sin((1 - x) * pi / 2)
