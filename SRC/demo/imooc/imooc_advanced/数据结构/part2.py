# 2-2 如何为元祖中的每个元素命名，提高程序可读性
student = ('Jim', 16, 'male', 'jim@gmail.com')
# name
print(student[0])
# age
if student[1] >= 18:
	pass
# sex
if student[2] == 'male':
	pass
# 代码中会充斥着0，1这样的元祖下标，不利于维护，能不能将其变为名字

# 1.定义类似于其他语言的枚举类型，也就是定义一系列数值常量
# 列表拆包形式：
NAME, AGE, SEX, EMAIL = range(4)
student = ('Jim', 16, 'male', 'jim@gmail.com')
print(student[NAME])
# age
if student[AGE] >= 18:
	pass
# sex
if student[SEX] == 'male':
	pass

# 2.使用标准库中collections.namedtuple替代内置tuple
from collections import namedtuple
#创建一个类的工厂
Student=namedtuple('Student',['name','age','sex','email'])
#按照位置传参
s=Student('Jim', 16, 'male', 'jim@gmail.com')
print(s)
#关键词传参
s2=Student(name='Jim', age=16, sex='male', email='jim@gmail.com')
print(s2)
#使用'.'的形式访问值
print(s.name,s.age,s.sex,s.email)
#namedtuple是tuple的一个子类
print(isinstance(s,tuple))
