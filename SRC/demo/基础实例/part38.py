# 题目：求一个3*3矩阵对角线元素之和。
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
from functools import reduce
from pprint import pprint
from random import randint

ss = [[randint(1, 100) for x in range(3)] for y in range(3)]
pprint(ss)

lst=[]
for x in range(3):
	for y in range(3):
		if x==y:
			lst.append(ss[x][y])

res=reduce(lambda x,y:int(x)+int(y),lst)
print(res)

