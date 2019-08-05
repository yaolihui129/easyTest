# 2-4 如何根据字典中值的大小，对字典中的项排序
#某班英语成绩以字典形式存储，根据成绩高低（值），计算学生的排名

#使用内置函数sorted
res=sorted([9,1,2,8,6])
print(res)

#随机构造一个成绩单
from random import  randint
res={x:randint(60,100) for x in 'xyzabc'}
print(res)
#直接对字典进行排序
# print(sorted(res))

#对字典进行转换，转换成可排序的
#(97,'a') ('69,'b') 元祖的比较的是第一个元素
#1.利用zip将字典数据转化元祖
res=zip(res.values(),res.keys())
res=list(res)
print(res)
res=sorted(res)
print(res)

#2.传递sorted函数的key参数
res={x:randint(60,100) for x in 'xyzabc'}
print(res.items())
#sorted第二个参数，key是待排序列表中的每项，允许传入一个lambda表达式，来说明通过哪项进行排序
res=sorted(res.items(),key=lambda x : x[1])
print(res)