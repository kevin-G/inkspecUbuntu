#!usr/bin/env python3
# -*- coding: utf-8 -*-

class Fib(object):
	"""docstring for Fib"""
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b =  1,1
			for x in xrange(n):
				a, b = b, a + b
			return a

		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			a, b = 1, 1
			L = []
			for x in xrange(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
 
f = Fib()
print f[0:5]
print f[:10]