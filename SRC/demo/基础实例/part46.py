# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。


def func(number):
	n=number
	while n*n>50:
		n=int(input('please input a int'))

func(50)