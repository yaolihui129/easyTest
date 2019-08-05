# coding=utf-8
import importlib
# import unittest


from SRC import settings



class BaseScene():
	'''
	场景类
	'''

	def __init__(self, testScene, logger, index):
		self.testCaseList = testScene.testCaseList  # 测试用例列表
		self.testClassList = None  # 测试用例对象列表
		self.logger = logger  # 日志对象
		self.index = index  # 场景编号
		self.sceneId = self.index + 1  # 场景ID

	def run(self):
		pass

	def getModule(self,testCase):
		testCaseDir = settings.TESTCASE['testCaseDir']
		p = testCase
		p = p[1:] if p[:1] == '/' else p
		if not p.startswith(testCaseDir):
			p = testCaseDir + p
		path = p
		path = path.replace('/', '.')
		path = path[1:] if path[:1] == '.' else path
		return path

