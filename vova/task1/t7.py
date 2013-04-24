#!/usr/bin/python2.7
from sys import stdin, stdout

s = stdin.readline()

i = 0
count = 0
while s[i] != '$':
	if s[i].isalnum():
		count += 1
	i += 1
print count
