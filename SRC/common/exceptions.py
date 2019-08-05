# coding=utf-8

class ScreenShotException(Exception):
	def __init__(self, msg=None):
		super(ScreenShotException, self).__init__()
		self.error = '截图发生异常'
		self.message = msg.msg.split('\n')[0][:150] if msg != None else ''


class ParamNumberException(Exception):
	def __init__(self, msg=None):
		super(ParamNumberException, self).__init__()
		self.error = '参数化文件中的参数个数不足'


class SwitchToWindowException(Exception):
	def __init__(self, msg=None):
		super(SwitchToWindowException, self).__init__()
		self.error = '切换窗口时发生异常，请检查窗口索引号是否正确'


class ReadParamFileException(Exception):
	def __init__(self, e, msg='',runResult='ERROR'):
		super(ReadParamFileException, self).__init__()
		self.info = '[ERROR-1010]:读取参数化配置文件引发的异常'
		self.msg = msg  # 信息
		self.e = e  # 错误对象
		self.runResult = runResult  # 运行结果

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)


class UploadFilePathException(Exception):
	def __init__(self, e='', msg=''):
		super(UploadFilePathException, self).__init__()
		self.info = '[ERROR-1013]:上传文件不存在引发的异常'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)


class JsonFormatException(Exception):
	def __init__(self, e='', msg=''):
		super(JsonFormatException, self).__init__()
		self.info = '[ERROR-0007-0]:期望的json与返回结果格式不一致.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)


class JsonValueException(Exception):
	def __init__(self, e='', msg=''):
		super(JsonValueException, self).__init__()
		self.info = '[ERROR-0007-1]:期望的json与返回结果的值不一致.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)


class JsonLoadsException(Exception):
	def __init__(self, e='', msg=''):
		super(JsonLoadsException, self).__init__()
		self.info = '[ERROR-0001-0]:解析json字符串引发的异常.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)


class ParamsException(Exception):
	def __init__(self, e='', msg=''):
		super(ParamsException, self).__init__()


class NotFoundParamsException(ParamsException):
	def __init__(self, e='', msg=''):
		super(NotFoundParamsException, self).__init__()
		self.info = '[ERROR-0008-0]:参数化配置文件中缺少必要参数.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)


class NotFindProjectClassException(ParamsException):
	def __init__(self, e='', msg=''):
		super(NotFindProjectClassException, self).__init__()
		self.info = '[ERROR-0008-1]:参数化配置文件中的项目简称不在interface_info.py配置文件中.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)


class RequestDataTypeException(ParamsException):
	def __init__(self, e='', msg=''):
		super(RequestDataTypeException, self).__init__()
		self.info = '[ERROR-0008-2]:参数化配置文件中的请求数据类型不在const.py配置文件中.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)


class RequestMethodException(ParamsException):
	def __init__(self, e='', msg=''):
		super(RequestMethodException, self).__init__()
		self.info = '[ERROR-0008-3]:参数化配置文件中的请求方法不在const.py配置文件中.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)

class ExpectTypeException(ParamsException):
	def __init__(self, e='', msg=''):
		super(ExpectTypeException, self).__init__()
		self.info = '[ERROR-0008-4]:参数化配置文件中的期待返回的数据类型不在const.py配置文件中.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)

class ResultCompareException(ParamsException):
	def __init__(self, e='', msg=''):
		super(ResultCompareException, self).__init__()
		self.info = '[ERROR-0008-5]:参数化配置文件中的结果对比不在const.py配置文件中.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)


class ResponseStatusCodeException(ParamsException):
	def __init__(self, e='', msg=''):
		super(ResponseStatusCodeException, self).__init__()
		self.info = '[ERROR-0009-0]:响应状态码异常.'
		self.msg = msg  # 信息
		self.e = e  # 错误对象

	def __str__(self):
		return '%s.%s.%s' % (self.info, self.msg, self.e)