# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)

class FibonacciSequence():
	def __init__(self, maxNumber):
		self.maxNumber = maxNumber

	def fibo(self, number):
		if number == 0:
			return 0
		if number == 1:
			return 1
		return self.fibo(number - 2) + self.fibo(number - 1)

	# def __iter__(self):
	# 	for x in range(self.maxNumber):
	# 		yield self.fibo(x)

	def __iter__(self):
		a=0
		b=1
		yield a
		yield b
		for x in range(3,self.maxNumber+1):
			a, b = b, a + b
			yield b

for x in  FibonacciSequence(1000):
	print(x)


