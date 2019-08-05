# coding:utf-8
import json

from SRC import settings

from SRC.common.const import TestType
from SRC.common.loga import putSystemLog
from SRC.test import interfaceTest
from SRC.test import uiTest


class Main():
	'''
	该类为easyTest项目的管理类
	'''

	def __init__(self, xml=None, testType='UI'):
		self.xmlPath = xml  # 接收的测试方案路径
		self.testType = testType  #测试类型，目前包含UI测试及接口测试
		self.uniqueCode = settings.UNIQUECODE  # 接收的唯一码

	def run(self):
		try:
			self.setTestType()  # 解析json设置测试类型（目前支持UI测试及接口测试）
		except Exception as e:
			pass
		else:
			self.start()

	def start(self):
		try:
			if self.testType == TestType.UI:
				uiTest.Main(self.xmlPath).run()
			elif self.testType == TestType.INTERFACE:
				interfaceTest.Main(self.xmlPath).run()
		except Exception as e:
			putSystemLog('[ERROR-0002-0]:选择测试方式时发生异常.%s' % e, None, False, '', '', True)

	def setTestType(self):
		settings.JSON_UNIQUECODE = None #外部传入的json唯一码
		if self.uniqueCode:
			try:
				settings.JSON_UNIQUECODE = json.loads(self.uniqueCode.replace("'", "\""))
			except Exception as e:
				putSystemLog('[ERROR-0001-0]:解析json字符串引发的异常.%s' % e, None, False, '', '', True)
				raise

			if settings.JSON_UNIQUECODE:
				try:
					self.testType = settings.JSON_UNIQUECODE['testType']  # 还没提供字段
				except Exception as e:
					putSystemLog('[ERROR-0001-1]:解析json字符串中testType发生异常.%s' % e, None, False, '', '', True)
					raise
