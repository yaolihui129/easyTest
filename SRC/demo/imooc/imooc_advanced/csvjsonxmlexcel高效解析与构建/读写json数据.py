# 使用标准库中的json模块，其中loads，dumps函数可以完成json数据的读写

import json

l=[1,2,'abc',{'name':'Bob','age':13}]
res=json.dumps(l)
print(res)

d={'b':None,'a':5,'c':'abc'}
print(json.dumps(d))

res=json.dumps(l,separators=[',',':'])
print(res)

res=json.dumps(d,sort_keys=True)
print(res)


l2=json.loads(res)
print(l2['c'])

with open('demo.json','w') as f:
	json.dump(l,f)