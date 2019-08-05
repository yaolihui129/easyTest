# 题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
# 程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。
import math


class SpecialNumber():
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def isPerfectSquare(self, number):
		res = int(math.sqrt(number))
		return res * res == number

	def getNumber1(self,number):
		return number+100
	def getNumber2(self,number):
		return number+268

	def __iter__(self):
		for x in range(self.start,self.end+1):
			n1=self.getNumber1(x)
			n2=self.getNumber2(x)
			if self.isPerfectSquare(n1) and self.isPerfectSquare(n2):
				yield x

for x in SpecialNumber(1,10000):
	print(x,end=',')