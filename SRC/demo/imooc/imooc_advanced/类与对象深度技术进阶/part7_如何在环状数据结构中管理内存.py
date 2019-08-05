# 如何在环状数据结构中管理内存
class A(object):
	def __del__(self):
		print('in A.__del')


a=A()
a2=a
import sys
res=sys.getrefcount(a)-1 #查看引用数量
print(res)


# 使用标准库weakref，它可以创建一种能访问对象但不增加引用计数的对象
import weakref
a_wref=weakref.ref(a)
a22=a_wref() #使用的时候在后面加（）
print(a is a22)
print(sys.getrefcount(a)-1)
del a
del a22


