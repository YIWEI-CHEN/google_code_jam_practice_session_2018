#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 22:40:06 2018

@author: yiwei
"""
import sys
import math

def bisection(left, right):
	if abs(left - right) == 1:
		return left
	return math.ceil((left + right) / 2)

def read_two_int():
	return list(map(int, input().split()))

def read_int():
	return int(input())

def read():
	return input()

def stderr(msg):
	print(msg, file=sys.stderr)

t = read_int()
error = False

for i in range(t):
	a, b = read_two_int()
	n = read_int()
	for x in range(n):
		guess = bisection(a, b)
		print(guess)
		sys.stdout.flush()
		s = read()

		# stderr('{i}: ({a}, {b}], {guess}, {s}'.format(i=i + 1, a=a, b=b, guess=guess, s=s))

		if s == 'TOO_BIG':
			b = guess
		elif s == 'TOO_SMALL':
			a = guess
		elif s == 'WRONG_ANSWER':
			error = True
			break
		elif s == 'CORRECT':
			break
	if error:
		break

sys.exit(0)

