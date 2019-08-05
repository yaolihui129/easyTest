# 如何拆分含有多种分隔符的字符串？
# 实际案例：我们要把某个字符串依据分隔符号拆分不同的字段，
# 该字符串包含多种不同的分隔符，例如：
# s='ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
# 其中<,>,<;>,<\>,<\t>都是分隔符号，如何处理？

s = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'


# 思考单一分隔符
# print(s.split())

# 方法一：连续使用str.split()方法，每次处理一种分隔符号
# 方法二：使用正则表达式的re.split()方法，一次性拆分字符串 （推荐）

# 方法一：
def mySplit(s, ds):
	res = [s]
	for d in ds:
		t = []
		for x in res:
			t.extend(x.split(d))
		res = t
	return [x for x in res if x]

res = mySplit(s, ';,|\t')
print(res)

#方法二：
import re
res=re.split('[,;\t|]+',s)
print(res)