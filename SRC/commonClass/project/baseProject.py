from SRC.common.exceptions import JsonFormatException, JsonValueException
from SRC.common.fileHelper import pathJoin


class BaseProject():
	def __init__(self, name, params, domain):
		self.name = name  # 项目名称
		self.params = params  # 请求的参数，对应xml参数文件的data字段，不一定是json类型
		self.domain = domain  # 网站根域名

	def getFullRequestData(self):
		'''
		返回一个完整的请求参数
		:return:
		'''
		pass

	def getFullUrl(self, url=None):
		if url:
			return pathJoin(self.domain, url)
		else:
			return self.domain

	def compareKey(self, expectJson, resultJson, equal=True):
		compareResult = (True, '')
		if isinstance(resultJson, list) and isinstance(expectJson, list):
			compareResult = (True, 'key对比:预期json与返回json都是列表')
		elif isinstance(resultJson, dict) and isinstance(expectJson, dict):
			expectList = [k for k in expectJson.keys()]
			resultList = [k for k in resultJson.keys()]
			res1 = [x for x in expectList if x not in resultList]
			if len(res1) > 0:
				compareResult = (False, 'key对比:返回json中不包含如下预期的key值:%s' % res1)
			elif equal:
				res2 = [x for x in resultList if x not in expectList]
				if len(res2) > 0:
					compareResult = (False, 'key对比:返回json中比预期json多了如下值:%s' % res2)
		else:
			compareResult = (False, 'key对比:预期json与返回json的类型不一致')
		return compareResult

	def compareFormat(self, expectJson, resultJson, equal=True):
		def compare(expect, result):
			if isinstance(expect, list) and isinstance(result, list):
				length = len(expect)
				if equal and length > len(result):
					raise JsonFormatException()
				else:
					for x in range(length):
						compare(expect[x], result[x])
			elif isinstance(expect, dict) and isinstance(result, dict):
				expectList = [k for k in expect.keys()]
				resultList = [k for k in result.keys()]
				res1 = [x for x in expectList if x not in resultList]
				if len(res1) > 0:
					raise JsonFormatException()
				elif equal:
					res2 = [x for x in resultList if x not in expectList]
					if len(res2) > 0:
						raise JsonFormatException()
				for x in expect.keys():
					compare(expect[x], result[x])

		try:
			compare(expectJson, resultJson)
		except JsonFormatException as e:
			return (False, e.info)
		except Exception as e:
			return (False, e)
		return (True, '')

	def compareAllValue(self, expectJson, resultJson, equal=True):
		def compare(expect, result):
			if isinstance(expect, list) and isinstance(result, list):
				length = len(expect)
				if equal and length > len(result):
					raise JsonFormatException()
				else:
					for x in range(length):
						compare(expect[x], result[x])
			elif isinstance(expect, dict) and isinstance(result, dict):
				expectList = [k for k in expect.keys()]
				resultList = [k for k in result.keys()]
				res1 = [x for x in expectList if x not in resultList]
				if len(res1) > 0:
					raise JsonFormatException()
				elif equal:
					res2 = [x for x in resultList if x not in expectList]
					if len(res2) > 0:
						raise JsonFormatException()
				for x in expect.keys():
					compare(expect[x], result[x])
			elif isinstance(expect, type(result)):
				if expect != result:
					raise JsonValueException()
			else:
				raise JsonFormatException()

		try:
			compare(expectJson, resultJson)
		except JsonFormatException as e:
			return False, e.info
		except JsonValueException as e:
			return False, e.info
		except Exception as e:
			return False, e
		return True, ''
