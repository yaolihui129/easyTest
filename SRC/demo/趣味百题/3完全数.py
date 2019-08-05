# 1.问题描述:
# 完全数（Perfect number)，又称完美数或完备数，是一些特殊的自然数。
# 它所有的真因子(即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
# 例如，
# 第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。
# 第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
# 编程求10000以内的完全数。
from functools import reduce

from SRC.demo.趣味百题.decorator import time_dec


@time_dec
def f(num):
	return [n for n in range(1, num) if
			reduce(lambda x, y: x + y, [x for x in range(1, n + 1) if n % x == 0][:-1], 0) == n]


print(f(10000))


