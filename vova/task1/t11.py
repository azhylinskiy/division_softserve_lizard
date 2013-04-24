#!/usr/bin/python2.7
from sys import stdin, stdout
from math import *

s = stdin.readline()
x = int(s)
i = x / 2

while i > 1:
	if x % i == 0:
		print i
	i = i - 1
