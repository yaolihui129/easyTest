# 题目：统计 1 到 100 之和。

def func(start,end):
	s=0
	for x in range(start,end+1):
		s+=x
	return s

print(func(1,100))