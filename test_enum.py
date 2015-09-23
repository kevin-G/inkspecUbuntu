#!usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

@unique
class Weekend(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = Weekend.Mon

print('day1 = ', day1)
print('Weekend.Tue = ', Weekend.Tue)
print('Weekend[\'Tue\'] =', Weekend['Tue'])
print('Weekend.Tue.value =', Weekend.Tue.value)
print('day1 == Weekend.Mon ?', day1 == Weekend.Mon)
print('day1 == Weekend.Tue ?', day1 == Weekend.Tue)
print('day1 == Weekend(1) ?', day1 == Weekend(1))

for name, member in Weekend.__members__.items():
	print(name, '=>', member)

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

TechnicalDepartment = Enum('people',('Victor', 'Kevin', 'Gary', 'Marie', 'Mike', 'Anna'))
for name, member in TechnicalDepartment.__members__.items():
	print(name, '=>', member, ',', member.value())
