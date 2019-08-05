# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　
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

for x in PrimeNumber(1,200):
	print(x)
