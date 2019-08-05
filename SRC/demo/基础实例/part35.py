# 题目：文本颜色设置。
# http://blog.chinaunix.net/uid-27714502-id-4110758.html

class Logger:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	FLASH='\033[5m'

	@staticmethod
	def log_normal(info):
		print(Logger.OKBLUE + info + Logger.ENDC)

	@staticmethod
	def log_high(info):
		print(Logger.OKGREEN + info + Logger.ENDC)

	@staticmethod
	def log_fail(info):
		print(Logger.FAIL + info + Logger.ENDC)

	@staticmethod
	def log_flash(info):
		print(Logger.FLASH+ info +Logger.ENDC)

Logger.log_normal('ok')
Logger.log_fail('error')
Logger.log_high('high')
Logger.log_flash('一闪一闪亮晶晶')