import json
from functools import reduce

from SRC.common.exceptions import JsonLoadsException
from SRC.common.fileHelper import isNoneOrEmpty
from SRC.common.utils import md5
from SRC.commonClass.project.baseProject import BaseProject
from SRC.interface_info import UDH


class UOrder(BaseProject):
	def __init__(self,params):
		super(UOrder, self).__init__(UDH['name'],params,UDH['domain'])
		self.appkey=UDH['appkey']
		self.token=UDH['token']
		self.secret=UDH['secret']
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
		self.__addRequired()
		sign=self.__getSign()
		self.__addSign(sign)
		return self.params

	def __getSign(self):
		'''
		获取签名
		签名算法如下：
		1.	对所有请求参数（包括appkey）进行字典升序排列
		2.	对以上排序后的参数表进行字符串连接:key1value1key2value2key3value3…keyNvalueN,如：appkeyxxxpageindexxxxpagesizexxxtokenxxx
		3.	将secret的值作为上面字符串连接的前缀和后缀，拼接后的结果如下：secretvalueappkeyxxxpageindexxxxpagesizexxxtokenxxxsecretvalue
		4.	对该字符串做MD5计算。
		5.	将计算结果转换为全大写形式后即可获取到签名串。

		签名串获取后，将其作为sign参数附加到对应的URL中，即可正常访问API。
		注意：请保证HTTP请求数据编码务必为UTF-8格式，URL也务必为UTF-8编码格式。

		:param params:
		:return:
		'''
		try:
			paramsList = sorted(self.params.items(), key=lambda item: item[0])
			sign = reduce(lambda x, y: x + y[0] + y[1], paramsList, '')
			sign = self.secret + sign + self.secret
			sign = md5(sign.encode())
			return sign.upper()
		except Exception as e:
			print(e)
			raise

	def __addRequired(self):
		'''
		向参数列表中添加appkey和token
		:return:
		'''
		if 'appkey' not in self.params.keys():
			self.params['appkey']=self.appkey
		if 'token' not in self.params.keys():
			self.params['token']=self.token

	def __addSign(self,sign):
		'''
		向参数列表中添加签名
		:param sign:
		:return:
		'''
		if 'sign' not in self.params.keys():
			self.params['sign']=sign
