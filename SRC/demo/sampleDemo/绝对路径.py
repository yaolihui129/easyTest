import os

res=os.path.isabs('c:/abc/bbb/c.txt')
print(res)


res=os.path.isabs('abc/bbb/c.txt')
print(res)

res=os.path.isabs('//abc/bbb/c.txt')
print(res)