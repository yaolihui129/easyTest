import functools


def funcName_dec(description):
	'''
	带参数的装饰器
	:param description:
	:return:
	'''

	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			ret = None
			try:
				ret = func(*args, **kwargs)
			except Exception:
				print(description)
			return ret

		return wrapper

	return decorator


def funcNameWithOutParam_dec(func):
	'''
	不带参数的装饰器
	:return:
	'''

	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		ret = None
		try:
			ret = func(*args, **kwargs)
		except Exception:
			pass
		return ret

	return wrapper
