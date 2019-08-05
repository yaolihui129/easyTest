# coding=utf-8
from SRC.unittest.case_interface import TestCase


class EasyCase(TestCase):
	def __init__(self, jsonParam):
		# 请不要修改该方法
		super(EasyCase, self).__init__(jsonParam)

	def beforeEasyRequest(self):
		super(EasyCase, self).beforeEasyRequest()
		'''
		发送请求前的操作写在这里
		'''

	def afterEasyRequest(self):
		super(EasyCase, self).afterEasyRequest()
		'''
		发送请求后的操作写在这里
		'''
