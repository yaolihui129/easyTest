# 2-5 如何快速找到多个字典中的公共键（key）
#西班牙足球甲级联赛，每轮球员进球统计按照字典形式存储，统计前N轮，每场比赛都有进球的球员

#随机取样函数 sample
from functools import reduce
from random import randint,sample
# s=sample('abcdefg',randint(3,6))
# print(s)

s1={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s2={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s3={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}

print(s1)
print(s2)
print(s3)

#一般方法找公共键 啰嗦，效率也不好
res=[]
for k in s1:
	if k in s2 and k in s3:
		res.append(k)

print(res)

#利用集合（set）的交集操作
#1.使用字典的viewkeys()/keys()方法，得到一个字典keys的集合。 适用于前3轮
# res1=s1.keys()
# print(res1)
res3=s1.keys() & s2.keys() & s3.keys()
print(res)
#2.使用map函数，得到所有字典的keys集合，适用于N轮
resN=map(dict.keys,[s1,s2,s3])
print(list(resN))

#3.使用reduce函数，取所有字典的keys的集合的交集
resNN=reduce(lambda a,b:a&b,map(dict.keys,[s1,s2,s3]))
print(list(resNN))

