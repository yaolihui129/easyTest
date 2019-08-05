# 题目：求100之内的素数。
import math


class PrimeNumber():
	def __init__(self,start,end):
		self.start=start if start>1 else 2
		self.end=end

	def isPrimeNumber(self,number):
		n=int(math.sqrt(number))
		for x in range(2,n+1):
			if number%x==0:
				return False
		return True

	def __iter__(self):
		for x in range(self.start,self.end+1):
			if self.isPrimeNumber(x):
				yield x

for x  in PrimeNumber(1,100):
	print(x)