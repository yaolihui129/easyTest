# 如何对迭代器做切片操作

# 实际案例：有某个文本文件，我们想读取其中某范围的内容如100~300行之间的内容，
# python中文本文件是可迭代对象，我们是否可以使用类似列表切片的方式得到一个
# 100~300行文件内容的生成器？
# f=open('')
# f[100:300] 可以吗

# 使用标准库中的itertools.islice,它能返回一个迭代对象切片的生成器

from itertools import islice

f=open('part1.py',encoding='utf-8')
# for x in f:
# 	print(f.readline())

for line in islice(f,2,5):
	print(line)

# islice(f,2) #前2行
# islice(f,2,None) #2行到最后

#消耗原生成器
l=range(20)
t=iter(l)
for x in islice(t,4,8,1):
	print(x,end=' ')

print()
for x in  t:
	print(x,end=' ')
