# 如何通过实例方法名字的字符串调用方法


# 某项目中，我们的代码使用了3个不同库中的图形类：
# Circle,Triangle,Rectangle
#
# 他们都有一个获取图形面积的接口（方法），但接口名字不同，
# 我们可以实现一个统一的获取面积的函数，使用每种方法名进行尝试，
# 调用相应类的接口
#
# 方法一：使用内置函数getattr，通过名字在实例上获取方法对象，然后调用
# 方法二：使用标准库operator下的methodcaller函数调用

# 方法一
# for name in ('area','getArea','get_area'):
# 	f=getattr(shape,name,None)
# 	if f:
# 		return f()


# 方法二
from operator import methodcaller
s='abc123abc456'
res=s.find('abc',4)
print(res)
f=methodcaller('find','abc',4)
res=f(s)
print(res)
