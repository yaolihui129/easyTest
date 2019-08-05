# 题目：将一个数组逆序输出。
from random import randint


def myReserved(lst):
	l=len(lst)
	if l%2==0:
		ll=l//2
	else:
		ll=(l+1)//2
	for x in range(ll):
		lst[x],lst[l-1-x]=lst[l-1-x],lst[x]


lst=[randint(1,100) for x in range(11)]
print(lst)
myReserved(lst)
print(lst)