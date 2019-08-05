# 带参数的装饰器
import functools

import time


def time_dec(func):
	'''
	统计函数执行时间
	:param func:
	:return:
	'''
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		ret = None
		sTime=time.time()
		try:
			ret = func(*args, **kwargs)
		except Exception as e:
			print(e)
		finally:
			eTime=time.time()
			print('use %.3fs'%(eTime-sTime))
		return ret

	return wrapper
