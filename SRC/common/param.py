# coding=utf-8
from SRC.common.const import INTERFACE_PARAMS
from SRC.common.fileHelper import isNoneOrEmpty


class Param():
	'''
	用于ui测试的参数类
	'''

	def __init__(self, dict):
		self.dict = dict
		self.setAttr()

	def setAttr(self):
		if self.dict != None:
			for k, v in self.dict.items():
				setattr(self, k, v)


class interFaceParam(Param):
	'''
	用于接口测试的参数类
	'''

	def __init__(self, dict):
		super(interFaceParam, self).__init__(dict)

	def checkParams(self):
		'''
		检查参数
		因为在接口测试中，有些参数是必须存在的，如果不存在，则报异常，无法继续执行
		:return:
		'''
		errParams = []
		for x in INTERFACE_PARAMS['mustContain']:
			if isNoneOrEmpty(getattr(self, x)):
				errParams.append(x)

		for x in INTERFACE_PARAMS['contain']:
			if isNoneOrEmpty(getattr(self, x)):
				setattr(self, x, '')
		return errParams