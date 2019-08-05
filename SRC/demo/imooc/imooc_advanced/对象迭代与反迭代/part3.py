# 3-3如何使用生成器函数实现可迭代对象
#实现一个可迭代对象的类，它能迭代出给定范围内所有的素数：
# pn=PrimeNumbers(1.30)
# for k in pn:
# 	print(k)

#解决方案：将该类的__iter__方法实现成生成器函数，每次yield返回一个素数


#什么是生成器函数？
#包含yield语句的函数是生成器函数，返回一个生成器对象
#生成器对象和迭代器对象在行为上很相似，都支持可迭代接口next
#函数内保留了运行的状态，第二次运行该函数，会从第一个yield后面继续走

#重点：
# 生成器对象支持可迭代接口next，同时还是可迭代对象，实现了iter,可以被遍历

def f():
	print('in f(),1')
	yield 1

	print('in f(),2')
	yield 2

	print('in f(),3')
	yield 3

#返回一个生成器对象
g=f()
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

#返回值就是他自身
# print(g.__iter__() is g)

#生成器函数是可迭代对象
# for x in g:
# 	print(x)



class PrimeNumber():
	def __init__(self,start,end):
		self.start=start
		self.end=end

	def isPrimeNumber(self,k):
		if k<2:
			return False

		for i in range(2,k):
			if k%i==0:
				return False
		return True

	def __iter__(self):
		for k in range(self.start,self.end+1):
			if self.isPrimeNumber(k):
				yield k


for x in PrimeNumber(1,100):
	print(x)


