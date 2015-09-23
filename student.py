#student.py

#!usr/bin/env python3
# -*- coding: utf-8 -*-

class student(object):

	def get_score(self):
		return self.score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('Score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self.score = value

s = student()

s.set_score(70)
print('the score is :', s.get_score())
