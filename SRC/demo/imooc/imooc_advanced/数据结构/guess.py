from random import randint
from time import sleep


def simple():
	print('猜数字游戏')
	target, min, max, index = randint(1, 100), 1, 100, 0
	while True:
		print('请输入一个数字(%s-%s):' % (min, max))
		try:
			number = int(input())
		except:
			print('输入错误，只能输入范围内的整数')
			continue
		if number < min or number > max:
			print('输入错误，只能输入范围内的整数')
			continue
		elif number > target:
			max = number
		elif number < target:
			min = number
		elif number == target:
			print('经过%s次的努力，恭喜你猜中了\r\n游戏结束' % (index + 1))
			break
		index = index + 1


def inputNumber(msg=''):
	while True:
		n = input(msg)
		if n.isdigit():
			return int(n)

def guessGame():
	# 定义玩家数量
	num = inputNumber('请输入玩家数量(1-10)：')
	players = ['player%s' % (x) for x in range(1, num + 1)]
	yourName = players[randint(0, num - 1)]
	print('本回合您的名字：%s\r\n' % (yourName))
	print('猜数字游戏开始：')
	target, min, max, index = randint(1, 100), 0, 101, 0
	while True:
		cPlayer = players[index % num]  # 当前玩家名称
		print('轮到[%s]了，当前数字范围(%s-%s)' % (cPlayer, min, max))
		if cPlayer == yourName:
			number = inputNumber('[%s]:请输入一个数字:' % (cPlayer))
		else:
			number = randint(min + 1, max - 1)
			print(number)
			sleep(0.5)

		if number <= min or number >= max:
			print('输入错误，只能输入范围内的整数')
			continue
		elif number > target:
			max = number
			print('大了')
		elif number < target:
			min = number
			print('小了')
		elif number == target:
			print('[%s]很不幸的猜中了结果，[%s]接受惩罚吧！\r\n游戏结束' % (cPlayer, cPlayer))
			break
		index = index + 1


if __name__ == '__main__':
	while True:
		guessGame()
		print('继续游戏吗(y)？')
		res = input()
		if res != 'y' and res != 'Y':
			break
