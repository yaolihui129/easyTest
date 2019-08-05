from collections import namedtuple
from random import randint


# data = [randint(-10,10) for _ in range(10)]
#
# res=filter(lambda x : x>=0,data)
#
# print(list(res))
#
# res=[x for x in data if x >=0]
#
# print(list(res))
#
# d={x:randint(60,100) for x in range(1,21)}
# print(d)
#
# dict={k:v for k,v in d.items() if v>90}
# print(dict)
#
# s=set(data)
# res={x for x in s if x%3==0}
# print(res)



# student = ('Jim', 16, 'male', 'jim@gmail.com')
# Student=namedtuple('Student',['name','age','sex','email'])
# s=Student('Jim', 16, 'male', 'jim@gmail.com')
# print(s)
# print(s.name)
# print(s.age)
# print(isinstance(s,tuple))

data=[randint(0,20) for _ in range(30)]
print(data)

c=dict.fromkeys(data,0)
from collections import Counter
c2=Counter(data)
print(c2)
res=c2.most_common(3)
print(res)


import re




