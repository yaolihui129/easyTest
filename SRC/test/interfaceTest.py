# coding=utf-8
import os
from collections import namedtuple
from threading import Thread

from SRC import settings
from SRC.common.const import RunModel, RunType, RunStatus, RunResult, TestType
from SRC.common.fileHelper import isNoneOrEmpty, pathJoin, isAbsolutePath, delsuffix, delFirstChar
from SRC.common.loga import putSystemLog
import xml.etree.ElementTree as ET

from SRC.commonClass.testPlan import TestPlan
from SRC.scene.interfaceScene import Scene
from SRC.test.baseTest import BaseTest

TestScene = namedtuple('testScene', ['sceneId', 'testCaseList'])


class Main(BaseTest):
	def __init__(self, xml=None, model='NORMAL'):
		super(Main, self).__init__(xml, model)
		self.testType = TestType.INTERFACE  # 该类为测试接口类
		self.testPlan = None  # 测试方案
		settings.TESTTYPE = TestType.INTERFACE

	def run(self):
		super(Main, self).run()

		testPlanName = self.xmlPath  # 测试方案文件名称
		putSystemLog('Interface程序启动.测试方案名称:%s' % testPlanName, None, False, '', '', True)
		try:
			self.setAbsoluteXmlPath()
			self.testPlan = TestPlan(self.xmlPath, self.testType)  # 创建测试方案对象
			self.setRunModel()  # 设置运行模式
			self.updateSettings()  # 根据运行模式更新settings设置
			self.testPlan.loadXml() # 从xml文件中读取测试方案
			self.start()  # 启动
		except Exception as e:
			putSystemLog('[ERROR-2001-0]:接口测试中未能有效捕获的异常.%s' % e, None, False, '', '', True)
		finally:
			putSystemLog('Interface程序启动程序结束.测试方案名称:%s\n' % testPlanName, None, False, '', '', True)

	def updateTestingModel(self):
		super(Main, self).updateTestingModel()

	def updateOnlineModel(self):
		super(Main, self).updateOnlineModel()

	def updateNormalModel(self):
		super(Main, self).updateNormalModel()

	def updateCommonSettings(self):
		super(Main, self).updateCommonSettings()

	def start(self):
		'''
		接口测试线程设置，这里有个想法，模拟多个线程是否可以实现压力测试，暂时不做
		:return:
		'''
		threadCount=settings.INTERFACE['threadCount']
		threads=[]
		files=range(threadCount)
		for _ in files:
			t=Thread(target=self.threadStart)
			threads.append(t)
		for i in files:
			threads[i].start()
		for i in files:
			threads[i].join()

	def threadStart(self):
		self.runTestPlan()

	def runTestPlan(self):
		'''
		运行测试方案
		:return:
		'''
		logger= self.createLoggerObj() #创建日志
		result = RunResult.PASS
		err = ''
		putSystemLog('Start.', logger, True, RunStatus.START, result, True, '开始')
		try:
			for index, scene in enumerate(self.testPlan.sceneList):
				Scene(scene, logger, index).run()
		except Exception as e:
			result = RunResult.ERROR
			err = e
		finally:
			putSystemLog('End.%s' % (err), logger, True, RunStatus.END, result, True, '结束')
