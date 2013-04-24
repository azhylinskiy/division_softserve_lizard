#!/usr/bin/python2.7
from sys import stdin, stdout

s = stdin.readline()
m, n, k, l = [int(x) for x in s.split()]

if m == k or n == l or (m - n) == (k - l) or (m + n) == (k + l):
	stdout.write("threatend")

