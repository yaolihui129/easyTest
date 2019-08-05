# coding=utf-8
import os

from SRC import settings
from SRC.common.const import RunModel
from SRC.common.fileHelper import pathJoin, isNoneOrEmpty, isAbsolutePath
from SRC.common.loga import putSystemLog, createLog
from SRC.common.loggernull import LoggerNull
from SRC.common.utils import createDir, getLogName


class BaseTest():
	def __init__(self, xml=None, model='NORMAL'):
		self.xmlPath = xml  # 接收的测试方案路径
		self.model = model  # 运行模式，分为normal正常 test 测试 注：测试模式下 不运行用例，只执行流程
		self.testPlan = []  # 测试方案列表
		self.sceneList = []  # 场景列表
		self.json = settings.JSON_UNIQUECODE  # 接收到的json参数

	def run(self):
		if isNoneOrEmpty(self.xmlPath):  # 当没有传入测试方案的时候，从控制台获取
			self.setTestPlanPathFromUser()

	def setTestPlanPathFromUser(self):
		'''
		控制台根据用户输入设置测试方案路径
		:return:
		'''
		filesList = []
		index = 0
		try:
			for dirPath, dirNames, fileNames in os.walk(settings.TESTCASE['xmlDir']):
				for filename in fileNames:
					if filename[-4:] == '.xml':
						filesList.append(
							(index + 1, filename, dirPath.replace('\\', '/').split(settings.SCRIPT_DIR)[1]))
						index += 1
			if len(filesList) == 0:
				print('%s目录下没有测试方案' % (settings.TESTCASE['xmlDir']))
				return
			print('%-3s %s' % ('编号', '测试方案'))
			for file in filesList:
				print('%-5s %s' % (file[0], pathJoin(file[2], file[1])))
			while True:
				result = input('请选择测试方案编号:')
				if result.isdigit():
					result = int(result) - 1
					if result >= 0 and result < len(filesList):
						self.xmlPath = filesList[int(result)][1]
						print('即将运行测试方案：%s' % (self.xmlPath))
						break
					else:
						print('输入错误')
				else:
					print('输入错误')
		except Exception as e:
			print(e)
			raise

	def setRunModel(self):
		'''
		设置运行模式
		:return:
		'''
		if self.json:  # 如果有传参，那么是实行线上模式
			self.model = RunModel.ONLINE

	def updateSettings(self):
		'''
		不同的模式绝对了运行方式
		TESTING：测试模式，不会运行真正的脚本（一般不使用该模式）
		ONLINE：在线模式，该模式下会向平台发送测试过程中的数据，默认不生成本地日志，如果传入json，则为该模式
		NORMAL:正常模式，该模式为本机运行，会生成本地日志
		
		'''
		if self.model == RunModel.TESTING:  # 测试模式
			self.updateTestingModel()

		if self.model == RunModel.ONLINE:  # 在线模式
			self.updateOnlineModel()

		if self.model == RunModel.NORMAL:  # 正常模式
			self.updateNormalModel()

		self.updateCommonSettings()

	def updateTestingModel(self):
		'''
		该方法内更新测试模式的全局设置
		:return:
		'''
		settings.RUNMODEL = self.model

	def updateOnlineModel(self):
		'''
		该方法内更新在线模式的全局设置
		:return:
		'''
		settings.RUNMODEL = self.model
		settings.REPORT['isWriteLog'] = False
		try:
			settings.SERVER['requestURL'] = self.json['requestURL']
		except Exception as e:
			putSystemLog('[ERROR-0001-2]:解析json字符串中requestURL发生异常.%s' % e, None, False, '', '', True)
			raise


	def updateNormalModel(self):
		'''
		该方法内更新正常模式的全局设置
		:return:
		'''
		settings.RUNMODEL = self.model

	def updateCommonSettings(self):
		'''
		该方法内更新通用设置
		'''
		if isNoneOrEmpty(settings.SERVER['requestURL']):  # 如果服务器url不正确，就不发送数据
			settings.SERVER['isRequest'] = False

	def setAbsoluteXmlPath(self):
		if not isAbsolutePath(self.xmlPath):
			self.xmlPath = pathJoin(settings.TESTCASE['xmlDir'], self.xmlPath)


	def start(self):
		pass

	def createLoggerObj(self):
		if settings.REPORT['isWriteLog']:
			# 创建日志对象
			logDir = createDir(settings.REPORT['logDir'])  # 创建日志目录
			logPath = os.path.join(logDir, getLogName())  # 日志绝对路径
			logger = createLog(logPath)  # 日志对象
		else:
			logger = LoggerNull()  # 定义一个空日志对象
		return logger

	def createScreenShotDir(self):
		screenShotDir = None
		if settings.REPORT['isScreenShot']:
			screenShotDir = createDir(settings.REPORT['screenShotDir'])  # 创建截图目录
		return screenShotDir