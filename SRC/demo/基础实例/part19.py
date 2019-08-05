# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# 程序分析：请参照程序Python 练习实例14。
import math


class PerfectNumber():
	def __init__(self,start,end):
		self.start=start
		self.end=end

	def isPerfectNumber(self,number):
		sqrtNumber=int(math.sqrt(number))
		res=0
		for x in range(1,sqrtNumber+1):
			if number%x ==0:
				res+=x+number//x
		return res==number*2


	def __iter__(self):
		for x in range(self.start,self.end+1):
			if self.isPerfectNumber(x):
				yield x


for x in PerfectNumber(1,10000):
	print(x)