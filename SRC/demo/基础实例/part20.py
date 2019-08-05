# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 程序分析：无

def func(high,downTime):
	length=0 #总长
	currentHigh=high
	for dTime in range(1,downTime+1):
		length+=currentHigh
		currentHigh/=2.0
		length+=currentHigh

	return length-currentHigh,currentHigh

print(func(100,2))