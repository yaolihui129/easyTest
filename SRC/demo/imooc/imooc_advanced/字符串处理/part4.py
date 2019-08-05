# 如何将多个小字符串拼接成一个大的字符串

# 方法一：迭代列表，连续使用'+'操作依次拼接每一个字符串。
# 方法二：使用str.join()方法，更加快速的拼接列表中所有字符串.(推荐)

s1='abcdefg'
s2='12345'

# 方法一运用的是运算符重载,实质调用str.__add__(s1,s2)
# print(s1+s2)
#造成大量浪费
pl=['<0112>','<32>','<1024*768>']
# s=''
# for p in pl:
# 	s+=p
# 	print(s)
# print(s)


#方法二：
print(';'.join(pl))

#列表表达式
l=['abc',123,45,'xyz']
print(''.join([str(x) for x in l]))

#生成器表达式，开销小
print(''.join(str(x) for x in l))