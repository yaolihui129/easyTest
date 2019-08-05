# 题目：利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，
# 60分以下的用C表示。
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
from random import randint


def getGrade(s):
	score = [90, 60, 0]
	grade = ['A', 'B', 'C']
	for x in range(len(score)):
		if s>=score[x]:
			return grade[x]

for x in range(40):
	s=randint(1,101)
	print(s,getGrade(s))