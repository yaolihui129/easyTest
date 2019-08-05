'''
首先，记住类型是属于对象的，而不是变量。
对象有两种：可更改与不可更改

可更改：list，dict
不可更改：strings，tuples，numbers

当一个引用传递给函数的时候,函数自动复制一份引用,这个函数里的引用和外边的引用没有半毛关系了.
'''


a = 1
def fun(a):
    a = 2
fun(a)
print(a) # 1

a = 1
def fun(a):
    a = 2
fun(a)
print(a)  # 1

a = []
def fun(a):
    a.append(1)
fun(a)
print(a)  # [1]

a = []
def fun(a):
    a.append(1)
fun(a)
print(a)  # [1]