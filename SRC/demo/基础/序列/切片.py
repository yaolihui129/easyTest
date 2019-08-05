numbers = [x for x in range(10)]
print(numbers)
#分片操作的实现需要提供两个索引作为边界，第1个索引的元素是包含在分片内的，第二个则不包含在分片内
print(numbers[3:6])
print(numbers[-7:6])

#复制整个序列
print(numbers[:])

#逆序一个序列
print(numbers[::-1])

# 列表的分片赋值,可以使用与原序列不等长的序列将分片替换
numbers[3:]=list('wangan')
print(numbers)

# 分片赋值可以在不需要替换任何原有元素的情况下插入新的元素
numbers[1:1]=list('tingting')
print(numbers)

#通过分片赋值来删除元素
numbers[1:-6]=[]
print(numbers)

