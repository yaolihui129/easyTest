# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于3时需考虑多加一天：
from functools import reduce


def getDaysInYear(year, month, day):
	DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	allDay = reduce(lambda x, y: x + y, DAYS[:month-1], 0) + day
	if isLeapYear(year) and month > 2:
		allDay += 1
	return allDay

def isLeapYear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			return year % 400 == 0
		else:
			return True
	else:
		return False

print(getDaysInYear(2016,12,31))