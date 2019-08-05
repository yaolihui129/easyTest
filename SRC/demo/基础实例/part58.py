# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的n个数
from random import randint



def move(s,n):
	s[len(s):]=s[:n]
	s[:n]=[]
	return s

s=[randint(1,100) for x in range(10)]
print(s)
s=move(s,3)
print(s)