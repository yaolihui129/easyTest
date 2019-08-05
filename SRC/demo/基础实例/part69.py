# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
from collections import Iterator, Iterable


class CircularQueue(Iterable):
	def __init__(self, lst):
		self.lst = lst
		self._pointer = [0]

	def delete(self):
		del self.lst[self._pointer[0] - 1]
		self._pointer[0] -= 1

	def __iter__(self):
		return CQueueIterator(self.lst, self._pointer)


class CQueueIterator(Iterator):
	def __init__(self, lst, pointer):
		self.lst = lst
		self.pointer = pointer

	def __next__(self):
		l = len(self.lst)
		if l == 0:
			raise StopIteration
		if self.pointer[0] >= l:
			self.pointer[0] = 0
		self.pointer[0] += 1
		return self.pointer[0] - 1


lst = [x for x in range(1, 35)]
c = CircularQueue(lst)
flag = 1
for x in c:
	if len(c.lst) == 1:
		break
	if flag % 3 == 0:
		c.delete()
	flag += 1
print(c.lst)
