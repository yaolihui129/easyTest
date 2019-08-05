# self：类实例自身的引用

# python中交换变量
import os
from pprint import pprint
from random import randrange

import sys

a,b=1,2
a,b=b,a
print(a,b)

# __buildins__模块，在程序开始或在交互解释器中给出提示之前，由解释器自动导入的

# python对象，python使用对象模型来存储数据，构造任何类型的值都是一个对象

# 类型包括：
# 整型、浮点、字符串、元祖、列表、字典
# 对象、None、集合、函数、模块、累

print(1//2)


print([randrange(1,10) for _ in range(10)])

print([1,2,3]*3)

print(max([1,2,3,4]))

print('wangan love tingting'.capitalize())

print(os.path.isabs('c:\\'))
print(sys.path)
pprint(sys.path)