#!/usr/bin/python2.7
from sys import stdin, stdout

s = stdin.readline()
m, n, k, l = [int(x) for x in s.split()]

if (m + n) % 2 == (k + l) % 2:
	stdout.write("same")
else:
	stdout.write("different")
