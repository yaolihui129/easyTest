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

		#登录
		# 此处指向data目录下登录.xml文件参数url
		driver.get('https://u8c-daily.yyuap.com/#/')
		driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div[2]/div/div[2]/span').click()
		sleep(3)
		#切换iframe
		iframe=driver.find_element_by_id('yhtloginIframe')
		driver.switch_to.frame(iframe)
		sleep(3)
		driver.find_element_by_id('username').clear()
		#此处指向data目录下登录.xml文件参数username
		# driver.find_element_by_id('username').send_keys(param.username)
		driver.find_element_by_id('username').send_keys('18500738046')
		driver.find_element_by_id('password').clear()
		# 此处指向data目录下登录.xml文件参数password
		#driver.find_element_by_id('password').send_keys(param.password)
		driver.find_element_by_id('password').send_keys('test111111')
		sleep(3)
		driver.find_element_by_id('submit_btn_login').click()
		sleep(5)
		title=driver.title
		if title=='数字化工作台':
			print('进入页面成功')
			sleep(5)




