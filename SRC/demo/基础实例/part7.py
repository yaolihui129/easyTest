# 题目：将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。

numbers=[x for x in range(10)]
n2=numbers[:]
n3=numbers
numbers[2]='abc'
del numbers
print(n2)

print(n3)
print(numbers)