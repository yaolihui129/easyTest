# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
# 程序分析：关键是计算出每一项的值。
from SRC.demo.趣味百题.decorator import time_dec


@time_dec
def func(number,count):
	if not isinstance(number,int):
		raise Exception('please input int ')
	n=str(number)
	if len(n)>1:
		raise Exception('please input one')
	res=0
	for x in range(1,count+1):
		res+=int(n*x)
	return res

print(func(2,1000))
