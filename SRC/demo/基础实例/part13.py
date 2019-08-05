# 题目：打印出所有的"水仙花数"，
# 水仙花数是指一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身。
# 例如：1^3+5^3+3^3=153。
# 求100~999之间所有的水仙花数。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
from functools import reduce


class NarcissisticNumber():
	def __init__(self,start,end):
		self.start=start
		self.end=end
	def isNarcissisticNumber(self,number):
		n=list(str(number))
		l=len(n)
		return reduce(lambda a,b:a+int(b)**l,n,0)==number

	def __iter__(self):
		for x in range(self.start,self.end+1):
			if self.isNarcissisticNumber(x):
				yield x

for x in NarcissisticNumber(100,9999):
	print(x)