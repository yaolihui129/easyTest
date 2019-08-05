# 问题描述:
# 220的真因数之和为1+2+4+5+10+11+20+22+44+55+110=284
# 284的真因数之和为1+2+4+71+142=220
# 毕达哥拉斯把这样的数对A、B称为相亲数：A的真因数之和为B，而B的真因数之和为A。
# 求100000以内的相亲数。
from functools import reduce

import math

from SRC.demo.趣味百题.decorator import time_dec

@time_dec
def f(num):
	def sum_yinzi(n):
		return reduce(lambda x, y: x + y, [x for x in range(1, n+1) if n % x == 0][:-1], 0)

	return [x for x in [(n, sum_yinzi(n)) for n in range(1, num + 1)] if x[0] < x[1] and x[0] == sum_yinzi(x[1])]


# print(f(10000))
@time_dec
def sum_yinzi(n):
	return reduce(lambda x, y: x + y, [x for x in range(1, n + 1) if n % x == 0][:-1], 0)

@time_dec
def sumOfFactors(k):
	p = 1
	q = k
	s = 0
	while p < q:
		if k % p == 0:
			s += p + q
		p += 1
		q = k / p

	if k == p * q and p == q:
		s += p

	return s - k

@time_dec
def fun(start, end):
	for x in range(start, end):
		y = sumOfFactors(x)
		if x < y and sumOfFactors(y) == x:
			print(x, y)


fun(2, 10000)
#
# res=sumOfFactors(1000000)
# print(res)
# res=sum_yinzi(1000000)
# print(res)