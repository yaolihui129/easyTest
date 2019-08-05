# coding=utf-8

# 水仙花数是指一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身。
# 例如：1^3+5^3+3^3=153。
# 求100~999之间所有的水仙花数。
from functools import reduce

from SRC.demo.趣味百题.decorator import time_dec


@time_dec
def f(start, end):
	return [x for x in range(start, end + 1) if reduce(lambda a, b: a + int(b) ** len(str(x)), str(x), 0) == x]


print(f(100, 10000))


class NarcissusNumber():
	def __init__(self,start,end):
		self.start=start
		self.end=end

	def isNarcissusNumber(self,number):
		if isinstance(number,int):
			n=str(number)
			figures=len(n)
			return reduce(lambda a,b:a+int(b)**figures,n,0)==number
		else:
			raise Exception('number is not type int.')

	def __iter__(self):
		for x in range(self.start,self.end+1):
			if self.isNarcissusNumber(x):
				yield x

@time_dec
def f2(start,end):
	for x in NarcissusNumber(start,end):
		print(x,end=',')

f2(100,10000)