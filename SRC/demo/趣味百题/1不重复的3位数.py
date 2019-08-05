# 1.问题描述:
# 0~9这10个数字可以组成多少不重复的3位数？
from SRC.demo.趣味百题.decorator import time_dec


@time_dec
def f(num):
	return [x for x in range(10 ** (num - 1), 10 ** num) if len(set(str(x))) == num]


print(f(3))


class NoRepeatNumber():
	def __init__(self, figures):
		self.figures = figures  # 位数

	def isNoRepeat(self, number):
		if not isinstance(number, int):
			raise Exception('number is not int')
		st = set(list(str(number)))
		return len(st) == self.figures

	def __iter__(self):
		start = 10 ** (self.figures - 1)
		end = 10 ** (self.figures) - 1
		for x in range(start, end):
			if self.isNoRepeat(x):
				yield x


for x in NoRepeatNumber(3):
	print(x,end=',')