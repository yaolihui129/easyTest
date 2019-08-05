# 2-1 如何在列表，字典，集合中根据条件筛选数据
# 通用做法：
data = [1, 5, -3, -2, 6, 8, 9]
res = []
for x in data:
	if x >= 0:
		res.append(x)
print(res)

#列表筛选元素
from random import randint
data = [randint(-10, 10) for _ in range(10)]
# 过滤掉data中的负数
# 1.filter
res=filter(lambda x: x >= 0, data)
print(list(res))
#2.通过列表解析(比filter快)
res=[x for x in data if x>=0]
print(list(res))

#字典筛选元素
d={x: randint(60,100) for x in range(1,21)}
print(d)
#根据value值过滤出分数高于90的同学
#3.字典解析
res={k:v for k,v in d.items() if v>=90}
print(res)

#4.集合解析
s =set(data)
res={x for x in s if x%3==0}
print(res)