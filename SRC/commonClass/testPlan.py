# coding=utf-8
import os
from collections import namedtuple

from SRC import settings
from SRC.common import xmlHelper
from SRC.common.const import RunStatus, RunResult, TestType
from SRC.common.fileHelper import isNoneOrEmpty, delsuffix, isAbsolutePath, delFirstChar
from SRC.common.loga import putSystemLog

TestScene = namedtuple('testScene', ['sceneId', 'testCaseList'])

class TestPlan():
	'''
	测试方案实体类
	目前包含UI测试与接口测试
	根据测试类型的不同个，从测试方案配置文件中读取的内容不同
	如果需要扩展，请根据原格式编写
	'''

	def __init__(self, xmlPath, testType):
		self.xmlPath = xmlPath  # 测试方案路径
		self.testType = testType  # 测试方案类型
		self.initData()  # 初始化数据容器

	def initData(self):
		'''
		初始化数据
		:return:
		'''
		self.sceneList = []  # 场景列表

		if self.testType == TestType.UI:
			self.hubDict = {}  # 用于UI测试
		elif self.testType == TestType.INTERFACE:
			pass

	def loadXml(self):
		try:
			tree = xmlHelper.read_xml(self.xmlPath)
			if self.testType == TestType.UI:#UI测试需要获取hub信息
				connection_nodes = xmlHelper.find_nodes(tree, settings.XML_TAG['testPlan']['connection'])
				if len(connection_nodes) > 0:
					self.setHubDict(connection_nodes[0])

			scene_nodes = xmlHelper.find_nodes(tree, settings.XML_TAG['testPlan']['scene'])
			if len(scene_nodes) > 0:
				self.setSceneList(scene_nodes)
		except Exception as e:
			putSystemLog('[ERROR-0003-0]:解析测试方案配置文件引发的异常.%s' % (e), None, True, RunStatus.END, RunResult.ERROR, True,
						 '异常')
			raise

	def setHubDict(self, connection_node):
		if len(self.hubDict) != 0:
			return
		hubDict = {}
		hub_nodes = xmlHelper.find_nodes(connection_node, settings.XML_TAG['testPlan']['hub'])
		hub_nodes = xmlHelper.get_node_by_keyvalue(hub_nodes, {settings.XML_TAG['testPlan']['enabled']: 'True'}, True)
		for hub in hub_nodes:
			browser = hub.get(settings.XML_TAG['testPlan']['browser'])
			if not isNoneOrEmpty(browser):
				remotePath = hub.text.strip() if hub.text is not None else ''
				hubDict[browser.lower().strip()] = remotePath
		self.hubDict = hubDict

	def setSceneList(self, scene_nodes):
		for scene_node in scene_nodes:
			sceneId=scene_node.get(settings.XML_TAG['testPlan']['sceneid'])
			settings.SCENEID = sceneId
			testCaseList = self.getTestCaseListInScene(scene_node)
			testScene = TestScene(sceneId, testCaseList)
			self.sceneList.append(testScene)

	def getTestCaseListInScene(self, scene_node):
		testCaseList = []
		testCase_nodes = xmlHelper.find_nodes(scene_node, settings.XML_TAG['testPlan']['testCase'])
		testCase_nodes = xmlHelper.get_node_by_keyvalue(testCase_nodes,
														{settings.XML_TAG['testPlan']['enabled']: 'True'}, True)
		# testCase_nodes = [node for node in testCase_nodes if not isNoneOrEmpty(node.text)] #是空的时候，调用内置的测试用例
		for testCase_node in testCase_nodes:
			testCasePath = self.getTestCasePath(testCase_node)
			paramPath = self.getParamPath(testCase_node)
			scriptId = self.getScriptId(testCase_node)
			testCaseList.append({'paramPath': paramPath, 'testCase': testCasePath, 'scriptId': scriptId})
		return testCaseList

	def getTestCasePath(self, testCase_node):
		path=testCase_node.text
		if isNoneOrEmpty(path):
			return None
		return delsuffix(path.strip(), '.py')  # 去掉后缀

	def getParamPath(self, testCase_node):
		paramPath = testCase_node.get(settings.XML_TAG['testPlan']['paramPath'])
		if not isNoneOrEmpty(paramPath):
			paramPath = delsuffix(paramPath.strip(), '.xml', False)  # 增加后缀
			if not isAbsolutePath(paramPath):
				paramPath = delFirstChar(paramPath, ['/', '\\'])
				paramPath = os.path.join(settings.PARAMETERIZATION['dataDir'], paramPath).replace('\\', '/')
		else:
			paramPath =None
		return paramPath

	def getScriptId(self,testCase_node):
		return testCase_node.get(settings.XML_TAG['testPlan']['scriptId'])  # 脚本id

