# 题目：利用递归方法求5!。
# 程序分析：递归公式：f(n)=f(n-1)*4!



def func(n):
	if n==0:
		return 1
	return n* func(n-1)

def cle(n):
	s=0
	for x in range(1,n+1):
		s+=func(x)
	return s

print(cle(3))
