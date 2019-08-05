# 如何让类支持比较操作

# 需要实现以下方法：
# __it__ 小于
# __le__小于等于
# __gt__ 大于
# __ge__大于等于
# __eq__等于
# __ne__不等于

# 使用标准库下的functools下的类装饰器total_ordering可以简化此过程

from functools import total_ordering
from abc import ABCMeta, abstractclassmethod


@total_ordering
class Shape(object):
	@abstractclassmethod
	def area(self):
		pass

	def __lt__(self, other):
		print('in __lt__')
		if not isinstance(other, Shape):
			raise TypeError('obj is not Shape')
		return self.area() < other.area()

	def __eq__(self, other):
		print('in __eq__')
		if not isinstance(other, Shape):
			raise TypeError('obj is not Shape')
		return self.area() == other.area()


class Rectangle(Shape):
	def __init__(self, w, h):
		self.w = w
		self.h = h

	def area(self):
		return self.w * self.h

class Circle(Shape):
	def __init__(self, r):
		self.r = r

	def area(self):
		return self.r ** 2 * 3.14


r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)
c1 = Circle(1)
print(r1 < r2)  # r1.__le__(r2)
print(r1 > r2)
print(r1 == r2)
print(r1 > c1)
