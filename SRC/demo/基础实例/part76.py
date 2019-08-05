# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n(利用指针函数)
from functools import reduce


def func(number):
	if  not isinstance(number,int):
		raise Exception('please input a int')
	start=2 if number%2==0 else 1
	s=0
	for x in range(start,number+1,2):
		s+=1/x
	return s

print(func(6))

