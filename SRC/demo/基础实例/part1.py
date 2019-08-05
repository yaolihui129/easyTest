# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
from pprint import pprint

from SRC.demo.趣味百题.decorator import time_dec


@time_dec
def func():
	res= [(i,j,k) for i in range(1,10) for j in range(1,10) for k in range(1,10) if i!=j and j!=k and i!=k]
	print(res)


func()
