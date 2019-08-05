# 题目：某个公司采用公用电话传递数据，
# 数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，
# 再将第一位和第四位交换，
# 第二位和第三位交换。
from functools import reduce


def func(number):
	if not isinstance(number,int):
		raise Exception('please input a int')
	n=str(number)
	lst=[(int(x)+5)%10 for x in n]
	print(lst)
	l=len(lst)
	if l%2==0:
		ll=l//2
	else:
		ll=(l+1)//2
	for x in range(ll+1):
		lst[x],lst[l-1-x]=lst[l-1-x],lst[x]
	print(lst)
	return reduce(lambda x,y:str(x)+str(y),lst,'')

print(func(1234))