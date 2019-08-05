# 2-3 如何统计序列中元素的出现频度？
#一，某随机序列中，找到出现次数最高的3个元素，他们出现的次数是多少？

#创建随机序列
from random import randint
data=[randint(0,20) for _ in range(30)]
print(data)

#通过data作为键，0作为值生成一个字典
c = dict.fromkeys(data,0)
print(c)

#1.每个数字出现的频度
for x in data:
	c[x]+=1
print(c)

#2.通过collections.Counter对象
#讲序列传入Counter的构造器，得到Counter对象是元素频度的字典
from collections import Counter
c2=Counter(data)
print(c2)
#Counter.most_common(n)方法得到频度最高的n个元素列表
res=c2.most_common(3)
print(res)

#二，对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，他们出现次数是多少？
import re
txt=open('httpd.conf').read()
print(txt)
#使用正则表达式的分隔模块对文章进行分隔
c3=Counter(re.split('\W+',txt))
print(c3)
res=c3.most_common(10)
print(res)