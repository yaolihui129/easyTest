# coding=utf-8
import functools
import json
import unittest as UT

import requests
import time

from SRC.common.const import RunStatus, RequestMethod, RequestDataType, RunResult, INTERFACE_PARAMS
from SRC.common.decorator import codeException_interface_dec
from SRC.common.exceptions import NotFoundParamsException, NotFindProjectClassException, RequestDataTypeException, \
	RequestMethodException, ResponseStatusCodeException, ExpectTypeException, ResultCompareException
from SRC.common.loga import putSystemLog, getJsonData, putLog
from SRC.common.param import interFaceParam
from SRC.common.utils import impClass, isAbsoluteUrl
from SRC.interface_info import projectClass

'''
接口测试用例
'''


class TestCase(UT.TestCase):
	def __init__(self, jsonParam):
		super(TestCase, self).__init__('runTest')
		self.__param = interFaceParam(jsonParam['paramsDict'])
		self.logger = jsonParam['logger']
		self.scriptId = jsonParam['scriptId']
		self.sceneId = jsonParam['sceneId']
		self.projectObj = None  # 包含产品信息的对象
		self.requestData = None  # 请求参数
		self.response = None  # 响应结果
		self.requestDuring = 0  # 请求消耗的时间

	@property
	def param(self):
		'''
		参数化驱动属性名称
		:return:
		'''
		return self.__param

	def setUp(self):
		putSystemLog('=' * 40, self.logger)
		putSystemLog('开始运行脚本%s' % (str(self.__class__)), self.logger)

	@codeException_interface_dec('1')
	def runTest(self):
		self.beforeEasyRequest()
		self.easyRequest()
		self.afterEasyRequest()

	def tearDown(self):
		putSystemLog('脚本运行完毕...', self.logger)
		putSystemLog('=' * 40+'\n', self.logger)

	def beforeEasyRequest(self):
		self.checkParams()  # 初始化并检查参数列表
		self.initProjectObj()  # 根据不同项目动态初始化对象
		self.initRequestData()  # 初始化请求参数数据

	def easyRequest(self):
		self.putInfoToLog()  # 输出基本数据
		startTime = time.time()
		self.request()
		endTime = time.time()
		self.requestDuring = endTime - startTime

	def afterEasyRequest(self):
		self.responseStatusCode()  # 根据响应值，判断请求是否发送成功
		self.compareResult()  # 结果对比

	def request(self):
		if self.param.method.upper() == RequestMethod.GET:
			self.response = requests.get(self.param.url, params=self.requestData)
		elif self.param.method.upper() == RequestMethod.POST:
			self.response = requests.post(self.param.url, data=self.requestData)

	def responseStatusCode(self):
		status_code = self.response.status_code
		if not status_code == 200:
			raise ResponseStatusCodeException('', status_code)
		self.putScriptLog(RunResult.PASS, 'status_code', self.requestDuring, '响应值:%s' % status_code)

	def initRequestData(self):
		self.setAbsoluteUrl()  # 设置完整url路径

		if self.param.dataType.upper() == RequestDataType.JSON:  # 请求类型为json
			self.requestData = self.getFullRequestJsonData()
		else:
			pass  # 待扩展

	def initProjectObj(self):
		project = impClass(projectClass[self.param.projectClass])  # 动态获取对象
		self.projectObj = project(self.param.data)  # 初始化一个项目对象

	def setAbsoluteUrl(self):
		if not isAbsoluteUrl(self.param.url):
			self.param.url = self.projectObj.getFullUrl(self.param.url)  # 获取完整的url

	def getFullRequestJsonData(self):
		return self.projectObj.getFullRequestData()

	def checkParams(self):
		'''
		检查并且设置参数
		:return:
		'''
		errParams = self.__param.checkParams()
		if len(errParams) > 0:
			raise NotFoundParamsException('', ''.join(errParams))
		if self.param.projectClass.lower() not in projectClass.keys():  # 判断项目名简称
			raise NotFindProjectClassException('', 'projectClass=%s' % self.param.projectClass)
		if self.param.dataType.lower() not in INTERFACE_PARAMS['dataType']:
			raise RequestDataTypeException('', 'dataType=%s' % self.param.dataType)
		if self.param.method.lower() not in INTERFACE_PARAMS['method']:
			raise RequestMethodException('', 'method=%s' % self.param.method)
		if self.param.expectType.lower() not in INTERFACE_PARAMS['expectType']:
			raise ExpectTypeException('', 'expectType=%s' % self.param.expectType)

		rc = set(self.param.resultCompare.split(','))
		resultCompare = [x for x in rc if x not in INTERFACE_PARAMS['resultCompare']]
		if resultCompare and len(resultCompare) > 0:
			raise ResultCompareException('', 'resultCompare=%s' % self.param.resultCompare)
		else:
			self.param.resultCompare = rc

	def putInfoToLog(self):
		putSystemLog('-' * 40, self.logger)
		putSystemLog('测试项目名称：%s(%s)' % (self.projectObj.name, self.param.projectClass), self.logger)
		putSystemLog('待测试接口：%s' % self.param.url, self.logger)
		putSystemLog('请求方式：%s' % self.param.method, self.logger)
		putSystemLog('请求数据类型：%s' % (self.param.dataType), self.logger)
		putSystemLog('返回数据类型：%s' % (self.param.expectType), self.logger)
		putSystemLog('结果对比：%s' % ','.join([INTERFACE_PARAMS['resultCompare'][x] for x in self.param.resultCompare]),
					 self.logger)
		putSystemLog('请求参数：%s' % (json.dumps(self.requestData, indent=4)), self.logger)
		putSystemLog('-' * 40, self.logger)

	def compare(self):
		'''
		继承该方法实现对比的重写
		:return:
		'''
		rc = self.param.resultCompare
		compareParam = [False, False, False, False]
		if len(rc) == 0 or '0' in rc:
			return None
		if '1' in rc:
			compareParam[0] = True
		if '2' in rc:
			compareParam[1] = True
		if '3' in rc:
			compareParam[2] = True
		if '4' in rc:
			if True not  in compareParam:
				compareParam = [True, True, True, True]
			else:
				compareParam[3] = True

		return self.compareJson(compareParam[0], compareParam[1], compareParam[2], compareParam[3])

	def compareJson(self, keyCompare=True, formatCompare=True, valueCompare=False, equal=False):
		try:
			expectJson = json.loads(self.param.expect.strip().replace("'", "\""))
			resultJson = json.loads(self.response.text.strip().replace("'", "\""))
			compareResult = (True, '')
			if keyCompare:
				compareResult = self.projectObj.compareKey(expectJson, resultJson, equal)
				if not compareResult[0]:
					return compareResult

			if formatCompare:
				compareResult = self.projectObj.compareFormat(expectJson, resultJson, equal)
				if not compareResult[0]:
					return compareResult

			if valueCompare:
				compareResult = self.projectObj.compareAllValue(expectJson, resultJson, equal)
				if not compareResult[0]:
					return compareResult

			return compareResult
		except:
			raise

	def compareResult(self):
		if self.param.expectType == RequestDataType.JSON:
			startTime = time.time()
			compareResult = self.compare()
			endTime = time.time()
			during = endTime - startTime

			if compareResult:
				if compareResult[0]:
					self.putScriptLog(RunResult.PASS, 'compareJson', during, 'JSON对比')
				else:
					self.putScriptLog(RunResult.ERROR, 'compareJson', during, 'JSON对比', compareResult[1])
			else:
				pass

	def putScriptLog(self, result, cmd, during, description, errorMessage=''):
		data = getJsonData(result,
						   cmd,
						   '',
						   errorMessage,
						   '%.3fs' % during if isinstance(during, float) else '',
						   '',
						   '',
						   description,
						   '',
						   '1',
						   self.sceneId,
						   self.scriptId)
		putLog(data, self.logger, self.sceneId)
