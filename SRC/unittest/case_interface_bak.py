# coding=utf-8
import functools
import json
import unittest as UT

import requests

from SRC import settings
from SRC.common.const import RunStatus, RequestMethod, RequestDataType, RunResult
from SRC.common.decorator import assert_dec, codeException_dec
from SRC.common.exceptions import JsonLoadsException
from SRC.common.fileHelper import isNoneOrEmpty
from SRC.common.loga import putSystemLog
from SRC.common.param import Param
from SRC.common.utils import impClass, isAbsoluteUrl
from SRC.interface_info import projectClass

'''
接口测试用例
'''


class TestCase(UT.TestCase):
	def __init__(self, jsonParam):
		super(TestCase, self).__init__('runTest')
		self.__param = Param(jsonParam['paramsDict'])
		self.logger = jsonParam['logger']
		self.scriptId = jsonParam['scriptId']
		self.projectObj = None  # 包含产品信息的对象
		self.requestData = None  # 请求参数
		self.response = None  # 响应结果

	@property
	def param(self):
		'''
		参数化驱动属性名称
		:return:
		'''
		return self.__param

	def setUp(self):
		putSystemLog('开始运行脚本%s' % (str(self.__class__)), self.logger)
		try:
			self.initProjectObj()  # 根据不同项目动态初始化对象
			self.initRequestData()  # 初始化请求参数数据
		except JsonLoadsException as e:
			putSystemLog(e, self.logger, True, RunStatus.RUNNING, RunResult.ERROR, True, '异常')
		except Exception as e:
			putSystemLog('[ERROR-2007-0]:测试用例初始化数据引发的异常.请检查参数是否配置正确%s' % e, self.logger, True, RunStatus.RUNNING,
						 RunResult.ERROR,
						 True, '异常')
			raise

	def initRequestData(self):
		dataType = self.param.dataType  # 请求类型
		if dataType == RequestDataType.JSON:  # 请求类型为json
			self.requestData = self.getFullRequestJsonData()

	def initProjectObj(self):
		project = impClass(projectClass[self.param.projectClass])  # 动态获取对象
		self.projectObj = project(self.param.data.replace("'", "\""))  # 初始化一个项目对象
		self.setAbsoluteUrl()  # 设置url

	def setAbsoluteUrl(self):
		if not isAbsoluteUrl(self.param.url):
			self.param.url = self.projectObj.getFullUrl(self.param.url)  # 获取完整的url

	def getFullRequestJsonData(self):
		return self.projectObj.getFullRequestData()

	@codeException_dec('3')
	def runTest(self):
		url = self.param.url
		method = self.param.method
		data = self.requestData

		putSystemLog('测试项目简称：%s' % (self.param.projectClass), self.logger, True, RunStatus.RUNNING, RunResult.PASS,
					 False, '测试项目简称')
		putSystemLog('待测试接口：%s' % (url), self.logger, True, RunStatus.RUNNING, RunResult.PASS, False, '待测接口')
		putSystemLog('请求方式：%s' % (method), self.logger, True, RunStatus.RUNNING, RunResult.PASS, False, '请求方式')
		putSystemLog('请求数据类型：%s' % (self.param.dataType), self.logger, True, RunStatus.RUNNING, RunResult.PASS, False,
					 '请求数据类型')
		putSystemLog('返回数据类型：%s' % (self.param.expectType), self.logger, True, RunStatus.RUNNING, RunResult.PASS, False,
					 '返回数据类型')
		putSystemLog('请求参数：%s' % (json.dumps(self.requestData,indent=4)), self.logger, True, RunStatus.RUNNING, RunResult.PASS, False,
					 '请求参数')

		if method == RequestMethod.GET:
			self.response = requests.get(url, params=data)
		elif method == RequestMethod.POST:
			self.response = requests.post(url, data=data)

	def compareResult(self):
		param = self.param
		r = self.response
		expectType = param.expectType
		putSystemLog('响应值：%s' % (r.status_code), self.logger, True, RunStatus.RUNNING, RunResult.PASS, True, '响应值')
		if expectType == RequestDataType.JSON:
			if isNoneOrEmpty(self.param.expect):
				pass
			else:
				compareResult = self.compare()
				putSystemLog('Json对比结果：%s,%s' % compareResult[0],compareResult[1], self.logger, True, RunStatus.RUNNING, RunResult.PASS, True,'Json对比结果')

		elif expectType == RequestDataType.STRING:
			putSystemLog(r.text, self.logger)

	def tearDown(self):
		self.compareResult()
		putSystemLog('脚本运行完毕...', self.logger)

	def compare(self):
		'''
		继承该方法实现对比的重写
		:return:
		'''
		return self.__compareJson(keyCompare=True, formatCompare=True, valueCompare=True, equal=False)

	def __compareJson(self, keyCompare=True, formatCompare=True, valueCompare=False, equal=False):
		try:
			expectJson = json.loads(self.param.expect.strip().replace("'", "\""))
			resultJson = json.loads(self.response.text.strip().replace("'", "\""))
			compareResult = (False, '')
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
