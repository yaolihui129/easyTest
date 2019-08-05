# coding=utf-8
from time import time, sleep

from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils


class EasyCase(TestCase):
	def __init__(self, webDriver, paramsList):
		# 请不要修改该方法124421
		super(EasyCase, self).__init__(webDriver, paramsList)

	@codeException_dec('3')
	def runTest(self):
		driver = self.getDriver()
		param = self.param
		tool  = utils


		# 登出
		sleep(3)
		driver.find_element_by_class_name('avatorImg').click()
		driver.find_element_by_xpath('//*[@id="home_header"]/span/div/div[3]/div[4]/span/div/div/div').click()



