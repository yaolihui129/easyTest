# 如何让对象支持上下文管理
# with open('demo.txt','w') as f:
from collections import deque
from sys import stdout, stdin
from telnetlib import Telnet


class TelnetClient():
	def __init__(self, addr, port=23):
		self.addr = addr
		self.port = port
		self.tn = None

	def start(self):
		self.tn = Telnet(self.addr, self.port)
		self.history = deque()

		# user
		t=self.tn.read_until('login:'.encode('utf-8'))
		stdout.write(t)
		user = stdin.readline()
		self.tn.write(user)

		# password
		t=self.tn.read_until(b'Password: ')
		if t.startswith(user[:-1]):
			t=t[len(user)+1]
		stdout.write(t)
		self.tn.write(stdin.readline())

		t=self.tn.read_until(b'$ ')
		stdout.write(t)
		while True:
			uinput =stdin.readline()
			if not uinput:
				break
			self.history.append(uinput)
			self.tn.write(uinput)
			t=self.tn.read_until(b'$ ')
			stdout.write(t[len(uinput)+1:])

	def cleanup(self):
		self.tn.close()
		self.tn=None
		with open(self.addr+'_history.txt','w') as f:
			f.writelines(self.history)

# client=TelnetClient('10.10.12.140',22)
# print('\nstart')
# client.start()
# print('\ncleanup')
# client.cleanup()



# 实现上下文管理协议，需定义实例的__enter__,__exit__方法，
# 他们分别子啊with开始和结束时被调用
# with对象 调用__enter__ 的返回值 作为as 后的变量
# 在__exit__中进行异常处理
# def __exit__(self,exc_type,exc_val,exc_tb):
	# return None 抛出异常
	# return True 不抛出异常
	# pass


