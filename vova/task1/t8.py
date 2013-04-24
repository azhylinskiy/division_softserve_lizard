#!/usr/bin/python2.7
from sys import stdin, stdout

s = stdin.readline()
i, k = [int(x) for x in s.split()]

if i % k == 0:
	print i - k
elif k % i == 0:
	print k - i
else:
	print i + k
