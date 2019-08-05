# 题目：暂停一秒输出。
from random import randint
from time import sleep

dct={k:randint(1,100) for k in 'xyz'}

for k,v in dct.items():
	print(k,v)
	sleep(1)