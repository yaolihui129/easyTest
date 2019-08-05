# 题目：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *


# print('%*s'%(4,'*'))
# print('%*s'%(5,'*'*3))
# print('%*s'%(6,'*'*5))
# print('%*s'%(7,'*'*7))

def printPic(maxLineNumber):
	if maxLineNumber%2==0:
		return
	start=(maxLineNumber+1)//2
	index=0
	for x in range(start,maxLineNumber+1):
		index += 1
		print('%*s'%(x,'*'*(2*index-1)))

	for x in range(maxLineNumber-1,start-1,-1):
		index -= 1
		print('%*s' % (x, '*' * (2 * index - 1)))


printPic(101)