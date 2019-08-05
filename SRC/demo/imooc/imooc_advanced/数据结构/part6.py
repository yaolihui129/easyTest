# 2-6 如何让字典保持有序
# 某编程竞赛记录成绩使用以下格式：
# {'Lilei':(2,38),'wanghong':(1,30)}
# 由于python中的字典默认不具备有序性
# OrderedDict按照字典输入的顺序排序
d = {}
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)
for k in d: print(k)
print()
from collections import OrderedDict

d = OrderedDict()
d['Jim'] = (1, 35)
d['Bob'] = (3, 40)
d['Leo'] = (2, 37)

for k in d: print(k, d[k])

# 模拟竞赛成绩举例
from time import time
from random import randint

d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in range(8):
	input()
	p = players.pop(randint(0, 7 - i))
	end = time()
	print(i + 1, p, end - start)
	d[p] = (i + 1, end - start)

print()
print('-' * 20)

for k in d:
	print(k, d[k])
