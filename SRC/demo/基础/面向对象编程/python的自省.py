print(type('333'))  # 返回任意对象的数据类型

print(str(['a', 1, 'abc']))  # 强制将数据转换为字符串

print(dir([]))  # 返回任意一个对象的属性和方法的列表：模块，函数，字符串，列表，字典.....

'''
综合：
type dir str, 以及所有其他的python内置函数一样被组合进入一个名字叫做__builtins__的特别模块中，
python启动的时候自动from __builtins__ import * 可以直接使用，
好处是，可以通过得到builtins的信息，作为一个组，存取所有内置的函数和属性,help函数实现了那个功能。
'''

print(getattr(['abc', 1], 'pop'))  # 使用getattr得到对象的各种引用

'''
三目运算符的实现：bool?a:b
Python 中很多时候，不允许使用if语句，一个负责的的程序猿应该将and or 技巧封装成函数：
'''


def choose(bool, a, b):
	return (bool and [a] or [b])[0]


res = choose(True, 1, 2)
print(res)

'''
使用lambda函数：快速定义单行的最小函数，可以被用在任何需要函数的地方，函数的语法通常与其他函数有点不同
可以接收任意多个参数（包括可选参数）值并且返回单个表达式的值的函数，
lambda函数不能包括命令，表达式不能超过一个，不要赛入过多东西。

lambda函数是风格问题，不一定非要使用，许多小的一行代码不会弄乱我的代码，用在需要特殊封装的，非重用的代码上。


'''

def f(x):
	return x * 2
print(f(2))

g=lambda x:x*2
print(g(2))

print((lambda x:x*2)(2))


'''
split及join的用法
空白格统一化
'''
myStr='My Name   is   xiao Ting       Ting'
print(myStr)
print(' '.join(myStr.split()))


'''
ljust的用法
'''
s='build'
print(s.ljust(30,'|'))
print(s.rjust(30,'|'))
print(s.ljust(2,'|')) #少于字符串，不更改

'''
打印列表
'''
li=['a','b']
print('\n'.join(li))



