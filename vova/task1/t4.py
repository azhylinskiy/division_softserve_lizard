#!/usr/bin/python2.7
from sys import stdin, stdout

s = stdin.readline()

i = 0
while s[i] != '@':
	if s[i] != 'A':
		stdout.write(s[i])
	i = i + 1
