# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
from random import randint

s=[randint(1,100) for x in range(10)]
s.sort()
print(s)

number=int(input('please input a int'))

if not isinstance(number,int):
	print('error')

# if number>s[-1]:
# 	s[len(s):]=[number]
# elif number<s[0]:
# 	s[0:0]=[number]
# else:
# 	for x in range(len(s)-1):
# 		if number>s[x] and number<s[x+1]:
# 			s[x+1:x+1]=[number]
# 			break
# print(s)

if number>=s[-1]:
	s.append(number)
elif number<=s[0]:
	s.insert(0,number)
else:
	for x in range(len(s)-1):
		if number>=s[x] and number<s[x+1]:
			s.insert(x+1,number)
			break
print(s)