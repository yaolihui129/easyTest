# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。
from functools import reduce


def func(n):
	s=0
	for x in range(1,n+1):
		s+=reduce(lambda x,y:x*y,[x for x in range(1,x+1)],1)
	return s


def func2(n):
	s=0
	t=1
	for x in range(1,n+1):
		t*=x
		s+=t
	return s

print(func2(3))
print(func(3))




