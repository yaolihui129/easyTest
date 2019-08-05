import json
from functools import reduce

from SRC.common.exceptions import JsonLoadsException
from SRC.common.fileHelper import isNoneOrEmpty
from SRC.common.utils import md5
from SRC.commonClass.project.baseProject import BaseProject
from SRC.interface_info import UDH, DEMO


class Demo1(BaseProject):
	def __init__(self,params):
		super(Demo1, self).__init__(DEMO['name'],params,DEMO['domain'])
		self.initParams()

	def initParams(self):
		if isNoneOrEmpty(self.params):
			self.params={}
		else:
			try:
				self.params=json.loads(self.params.replace("'", "\"")) #可能会报异常
			except Exception as e:
				raise JsonLoadsException(e)

	def getFullRequestData(self):
		'''
		在这里根据接口文档获取完整的请求数据
		:return:
		'''
		return self.params
