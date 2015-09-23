#!usr/bin/env python3
# -*- coding: utf-8 -*-

# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self, arg):
# 		super(Student, self).__init__()
# 		self.arg = arg

# s = Student('Victor')

# print ('my name is %s' % s.arg)



class Student(object):
	"""docstring for Student"""
	def __init__(self, arg):
		super(Student, self).__init__()
		self.arg = arg
		
	def __call__(self):
			print('my name is %s' % self.arg)

s = Student('Kevin')

s()

print('Student is a object is %s!' % callable(Student('Kevin')))
print('__call__ is a object is %s!' % callable('1,2,3'))