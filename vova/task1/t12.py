#!/usr/bin/python2.7
from sys import stdin, stdout

s = stdin.readline()
r = float(s)

while True:
	op = stdin.readline()
	s = stdin.readline()
	x = float(s)
	if op[0] == '+':
		r = r + x
	elif op[0] == '-':
		r = r - x
	elif op[0] == '*':
		r = r * x
	elif op[0] == '/':
		r = r / x
	print r
