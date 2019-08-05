# coding:utf-8

from threading import Thread

from selenium.webdriver import DesiredCapabilities

from SRC import settings
from SRC.common.const import Agent, RunType, BROWSER_ID, RunStatus, RunResult, TestType
from SRC.common.fileHelper import isNoneOrEmpty, astrcmp
from SRC.common.loga import putSystemLog, getRecordTxt, manageLogRecord
from SRC.commonClass.testPlan import TestPlan
from SRC.scene.uiScene import Scene
from SRC.test.baseTest import BaseTest
from SRC.webdriver.browser import Browser


class Main(BaseTest):
	'''
	该类为UI测试类
	'''

	def __init__(self, xml=None, model='NORMAL'):
		super(Main, self).__init__(xml, model)
		self.testType = TestType.UI  # 该类为ui测试类
		self.testPlan = None  # 测试方案
		settings.TESTTYPE = TestType.UI

	def run(self):
		super(Main, self).run()
		testPlanName = self.xmlPath  # 测试方案文件名称
		putSystemLog('UI程序启动.%s' % testPlanName, None, False, '', '', True)
		try:
			self.setAbsoluteXmlPath()
			self.testPlan = TestPlan(self.xmlPath, self.testType)  # 创建测试方案对象
			self.setRunModel()  # 设置运行模式
			self.updateSettings()  # 根据运行模式更新settings设置
			self.testPlan.loadXml()  # 从xml文件中读取测试方案
			self.start()  # 启动
		except Exception as e:
			putSystemLog('[ERROR-1017]:未记录情况引发的异常.%s' % e, None, False, '', '', True)
		finally:
			putSystemLog('UI程序结束.%s\n' % testPlanName, None, False, '', '', True)

	def updateTestingModel(self):
		super(Main, self).updateTestingModel()
		settings.TESTCASE['runType'] = RunType.BROWSER

	def updateOnlineModel(self):
		super(Main, self).updateOnlineModel()
		try:
			hubDict = {}
			for browser in self.json['browsers'].keys():
				br = browser.lower()[:2]
				if br in BROWSER_ID:
					hubDict[br] = self.json['browsers'][browser]
					break
			self.testPlan.hubDict = hubDict  # 在线模式下，hub由外部参数传入
		except Exception as e:
			putSystemLog('[ERROR-1015]:解析json字符串时引发的异常.%s' % e, None, False, '', '', True)
			raise

		settings.TESTCASE['runType'] = RunType.REMOTE

	def updateNormalModel(self):
		super(Main, self).updateNormalModel()

	def updateCommonSettings(self):
		super(Main, self).updateCommonSettings()

	def start(self):
		# 配置场景
		try:
			runType = settings.TESTCASE['runType']
			if astrcmp(runType, RunType.REMOTE):
				self.remote_start()
			elif astrcmp(runType, RunType.BROWSER):
				self.browser_start()
		except Exception as e:
			putSystemLog('[ERROR-1003]:配置场景引发的异常.%s' % (e), None, True, RunStatus.END, RunResult.ERROR, True, '异常')
			raise

	def browser_start(self):
		# 线下模式
		for br, host in self.testPlan.hubDict.items():
			driver = Browser(self.switchBrowser(br)).driver()
			self.runTestPlan(driver)

	def remote_start(self):
		# 线上模式
		threads = []
		files = range(len(self.testPlan.hubDict))
		# 创建线程
		for browser, host in self.testPlan.hubDict.items():
			browser = self.switchBrowser(browser)
			t = Thread(target=self.threadStart, args=(browser, host))
			threads.append(t)

		# 启动线程
		for i in files:
			threads[i].start()
		for i in files:
			threads[i].join()

	def threadStart(self, browser, host):
		desiredCapabilities = self.setDesiredCapabilities(browser)
		driver = Browser(Agent.REMOTE, command_executor=host,
						 desired_capabilities=desiredCapabilities).driver()
		self.runTestPlan(driver)

	def runTestPlan(self, driver):
		logger = self.createLoggerObj()  # 创建该场景日志对象
		screenShotDir = self.createScreenShotDir()  # 创建截图目录
		result = RunResult.PASS
		err = ''
		putSystemLog('Start.', logger, True, RunStatus.START, result, True, '开始')
		try:
			for index, scene in enumerate(self.testPlan.sceneList):
				Scene(driver, scene, logger, screenShotDir, index).run()
		except ConnectionRefusedError as e:
			pass
		except Exception as e:
			result = RunResult.ERROR
			err = e
		finally:
			putSystemLog('End.%s' % (err), logger, True, RunStatus.END, result, True, '结束')
			putSystemLog(getRecordTxt(manageLogRecord(operator='get'), type='all'), logger)  # 写入统计结果

	def switchBrowser(self, key):
		browser = Agent.FIREFOX
		try:
			if key[:2] == BROWSER_ID[0]:
				browser = Agent.FIREFOX
			elif key[:2] == BROWSER_ID[1]:
				browser = Agent.CHROME
			elif key[:2] == BROWSER_ID[2]:
				browser = Agent.IE
		except:
			pass
		return browser

	def setDesiredCapabilities(self, browser):
		if browser == Agent.CHROME:
			desiredCapabilities = DesiredCapabilities.CHROME.copy()
			chrome_options = {}
			chrome_options['args'] = ['--disable-popup-blocking']
			chrome_options['excludeSwitches'] = ['ignore-certificate-errors']
			desiredCapabilities['chromeOptions'] = chrome_options
		elif browser == Agent.IE:
			desiredCapabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
		else:
			desiredCapabilities = DesiredCapabilities.FIREFOX.copy()

		return desiredCapabilities
