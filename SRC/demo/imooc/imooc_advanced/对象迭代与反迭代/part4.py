#如何进行反向迭代以及如何实现反向迭代

# 实际案例：实现一个连续浮点数发生器FloatRange(和xrange类似)，根据给定的范围(start,end)
# 和步进值(step)产生一系列连续浮点数，如迭代FloatRange(3.0,4.0,0.2)可产生序列：
# 正向：3.0 3.2 3.4
# 反向：4.0,3.8 3.6

#
# class FloatRange():
# 	def __init__(self,start,end,step):
# 		self.start=start
# 		self.end=end
# 		self.step=step
# 		self.current=start
#
# 	def __iter__(self):
# 		while self.current<=self.end:
# 			self.current+=self.step
# 			yield self.current
# #
# for x in FloatRange(3.0,4.0,0.2):
# 	print('%.1f'%x,end=',')


# 生成器和生成式的区别
# 生成器返回一个对象
# 生成式返回一个序列


#如何反向得到一个列表
# l=[1,2,3,4,5]
# print(reversed(l))
# print(iter(l))

# 正向实现__iter__方法
# 反向实现__reversed__方法

class FloatRange():
	def __init__(self,start,end,step=0.1):
		self.start=start
		self.end=end
		self.step=step

	def __iter__(self):
		t=self.start
		while t<=self.end:
			yield t
			t+=self.step

	def __reversed__(self):
		t =self.end
		while t>=self.start:
			yield t
			t-=self.step

for x in FloatRange(1.0,4.0,0.5):
	print(x,end=',')

print()
for x in reversed(FloatRange(1.0,4.0,0.5)):
	print(x,end=',')



