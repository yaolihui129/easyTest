# coding=utf-8
from SRC.common.decorator import codeException_dec
from SRC.common import utils_user
from SRC.unittest.case_interface import TestCase


class EasyCase(TestCase):
	def __init__(self, jsonParam):
		# 请不要修改该方法
		super(EasyCase, self).__init__(jsonParam)

	@codeException_dec('3')
	def initData(self):
		tool=utils_user
		'''
		初始化参数数据
		:return:
		'''
		pass
