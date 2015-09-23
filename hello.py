#use_slots.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
	__slots__ = ('name', 'age')

class GraduateStudent(Student):
	pass

s = Student()
s.name = 'Kevin'
s.age = 34
try:
	s.score = 99
except AttributeError as e:
	print ('AttributeError:', e)

g =  GraduateStudent()
g.score = 99
print('g.score = ', g.score)