# 题目：809*??=800*??+9*??+1 其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。

def func():
	for x in range(10,100):
		if 809*x==800*x+9*x+1:
			return x
	return 'error'

print(func())
