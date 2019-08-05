import importlib
import os
from time import time
from unittest import TestSuite
import xml.etree.ElementTree as ET
from SRC import settings
from SRC.common import xmlHelper
from SRC.common.const import RunResult, RunStatus, RunModel
from SRC.common.exceptions import ReadParamFileException
from SRC.common.fileHelper import isNoneOrEmpty
from SRC.common.loga import putSystemLog, manageLogRecord, getRecordTxt
from SRC.scene.baseScene import BaseScene
from SRC.commonClass.interface.subTestCase import EasyCase
from SRC.unittest.case_interface import TestCase
from SRC.unittest.runnerExt import TextTestRunner


class Scene(BaseScene):
	'''
	场景类
	'''

	def __init__(self, testScene, logger, index):
		super(Scene, self).__init__(testScene, logger, index)

	def run(self):
		logger = self.logger  # 日志对象
		runTime = settings.PARAMETERIZATION['runTime']  # 单个场景运行次数
		runModel = settings.RUNMODEL  # 运行模式

		sceneDes = '场景<%d>开始.' % (self.sceneId) if runTime == 1 else '场景<%d>开始.该场景共运行%d次' % (self.sceneId, runTime)
		putSystemLog(sceneDes, logger)
		manageLogRecord(self.sceneId, operator='create')  # 创建统计记录

		self.importTestCase(self.testCaseList)  # 引入测试用例

		if len(self.testClassList) == 0:
			putSystemLog('[ERROR-2004-0]:场景<%d>中不包含任何测试用例' % self.sceneId, logger, False, RunStatus.RUNNING,
						 RunResult.ERROR, True)
			return

		if runModel == RunModel.TESTING:
			putSystemLog('启动测试模式下，不会真正运行测试用例的脚本！', logger)



		sTime = time()
		for x in range(runTime):
			try:
				if runTime != 1:
					putSystemLog('第%d次运行：' % (x + 1), logger)
				putSystemLog('开始加载脚本...', logger)
				suite = self.suiteFactory()  # 创建并配置测试单元套件
				putSystemLog('脚本加载完成...\n', logger)
				if runModel != RunModel.TESTING and len(suite._tests) > 0:
					TextTestRunner().run(suite)
			except Exception as e:
				putSystemLog('[ERROR-2006-0]:测试套件运行失败引发的异常.%s' % e, logger, True, RunStatus.RUNNING, RunResult.ERROR,
							 True, '异常')
		eTime = time()
		putSystemLog('场景<%d>结束.用时:%.3fs.' % (self.sceneId, eTime - sTime), logger)
		putSystemLog(getRecordTxt(manageLogRecord(self.sceneId, operator='get')), logger)
		# putSystemLog('-' * 40, logger)

	def importTestCase(self, testCaseList):
		'''
		动态添加测试用例的引用
		由于参数化文件中包含接口测试的必选项
		所以每一条测试用例，必须包含参数化文件，但脚本不是必须的
		如果不包含脚本，会加载默认的测试用例脚本
		:param testCaseList:
		:return:
		'''
		classList = []
		for index, dict in enumerate(testCaseList):
			paramPath=dict['paramPath']
			if not paramPath  :
				err = '[ERROR-2002-0]:场景<%d>-用例<%d>,未发现参数化文件,该用例被忽略.' % (self.sceneId,index)
				putSystemLog(err, self.logger, True, RunStatus.RUNNING, RunResult.ERROR, True)
				continue

			model_module = None
			try:
				p = dict['testCase']
				if p:
					path = self.getModule(p)
					model_module = importlib.import_module(path)  # 引入模块
			except Exception as e:
				err = '[ERROR-2003-0]:引入测试方案模块失败引发的异常.%s.%s' % (dict['testCase'], e)
				putSystemLog(err, self.logger, True, RunStatus.RUNNING, RunResult.ERROR, True)
				continue
			if model_module:
				'''
				配置文件中有脚本的时候，根据脚本创建测试用例对象
				'''
				for attr_name in dir(model_module):
					attr = getattr(model_module, attr_name)
					try:
						if issubclass(attr, TestCase) and attr.__name__ != TestCase.__name__:
							classList.append(
								{'paramPath': dict['paramPath'], 'testClass': attr, 'className': attr.__name__,
								 'scriptPath': '%s' % (p), 'scriptId': dict['scriptId']})
					except Exception:
						continue
			else:
				'''
				配置文件中没有脚本的是，创建默认测试用例对象
				'''
				classList.append(
					{'paramPath': dict['paramPath'], 'testClass': EasyCase, 'className': EasyCase.__name__,
					 'scriptPath': None, 'scriptId': dict['scriptId']})
		self.testClassList = classList

	def suiteFactory(self):
		suite = TestSuite()  # 创建测试单元套件
		for index, testCaseClass in enumerate(self.testClassList):
			try:
				paramPath = testCaseClass['paramPath']  # 获取参数文件地址
				if paramPath and os.path.exists(paramPath):
					paramsList = self.readParamXml(paramPath, testCaseClass['className'])
				else:
					continue  # 接口测试必须传入参数文件

				for i, params in enumerate(paramsList):
					if len(params)==0:
						continue

					scriptId = testCaseClass['scriptId'] if testCaseClass['scriptId'] else ''  # 添加临时脚本id
					jsonParam = {'scriptId': scriptId,
								 'paramsDict': params,
								 'logger': self.logger,
								 'sceneId':self.sceneId}  # 传递给测试用例的参数
					suite.addTest(testCaseClass['testClass'](jsonParam))  # 创建测试用例，并添加到套件中

					putSystemLog('脚本<%d_%d>：加载成功.' % (index + 1, i + 1), self.logger)
					# putSystemLog('脚本<%d_%d>参数列表：' % (index + 1, i + 1), self.logger)
					# for k, v in params.items():
					# 	putSystemLog("%s:%s" % (k, v), self.logger)
			except ReadParamFileException as e:
				putSystemLog(e, self.logger, True, RunStatus.RUNNING, RunResult.ERROR, True)
			except Exception as e:
				err = '[ERROR-2005-0]:向测试单元套件添加测试用例对象时引发的异常.%s.%s' % (testCaseClass['scriptPath'], e)
				putSystemLog(err, self.logger, True, RunStatus.RUNNING, RunResult.ERROR, True)
		return suite

	def readParamXml(self, paramPath, className='EasyCase'):
		# 读取参数xml文件的数据
		paramsList = []  # 参数化测试用例的列表

		try:
			tree = xmlHelper.read_xml(paramPath)
			testCase_nodes = xmlHelper.find_nodes(tree, settings.XML_TAG['testParam']['testCase'])
			for testCase_node in testCase_nodes:
				testClass_node = xmlHelper.find_nodes(testCase_node, "testClass[@name='EasyCase']")[0]
				params = {}
				for param in testClass_node:
					id = param.get(settings.XML_TAG['testParam']['id'])
					if not isNoneOrEmpty(id):
						value = param.text or ''
						params[id] = value
				paramsList.append(params)
		except Exception as e:
			raise ReadParamFileException(e)
		return paramsList
