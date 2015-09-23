#decorator.py
#!usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import functools

def log(func):
	@functools.wraps(func) 
	def wrapper(*args, **kw):
	 	print('call %s():' % func.__name__)
	 	return func(*args, **kw)
	return wrapper
	
@log
def now():
	print time.strftime('%Y-%m-%d %A %X %Z', time.localtime(time.time()))

now()   #  call this function


def logger(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
		 	print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator	
	
@logger('DEBUG')
def today():
	print time.strftime('%Y-%m-%d %A %X %Z', time.localtime(time.time()))

today()   #  call this function
print(today.__name__)