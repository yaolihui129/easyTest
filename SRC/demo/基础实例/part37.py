# 题目：对10个数进行排序。
from random import randint

s=[randint(1,100) for x in range(10)]

l=len(s)
print(s)
for x in range(l):
	for y in range(x,l):
		if s[x]>s[y]:
			s[x],s[y]=s[y],s[x]

print(s)