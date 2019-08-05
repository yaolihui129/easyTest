# 3-1 如何实现可迭代对象和迭代器对象？
# 可迭代对象：实现了__iter__()方法或者__getitem__()方法
l = [1, 2, 3, 4]
s = 'abcde'

for x in l: print(x)
for x in s: print(x)

# for循环的原理：
# 1.in后面是可迭代对象，通过iter(l)得到一个迭代器对象
# 2.不停的调用迭代器对象中的__next__接口获取列表或序列中的值
# 3.直到最终捕获到StopIteration异常，for循环结束

print(iter(l))
print(iter(s))
# print(iter(5)) #int不是可迭代对象

# 列表和字符串满足了某种特殊的接口
# l.__iter__() #可迭代接口
# s.__getitem__() #序列接口

# 迭代器对象满足的接口 __next__()
t = iter(l)
t.__next__()
