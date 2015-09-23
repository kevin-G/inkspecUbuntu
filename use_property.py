#use_property.py
#!usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	"""docstring for Student"""

	@property
	def score(self):
	    return self._score
	
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('Score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

s = Student()
s.score = 60
print('the score is :', s.score)
s.score = 9999