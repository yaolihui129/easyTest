import json
import pprint
from functools import reduce

import requests

from SRC.common.fileHelper import pathJoin
from SRC.common.utils import md5, impClass

# from SRC.commonClass.project.uOrder import UOrder
from SRC.interface_info import projectClass

secret = '7387d49874dadd02184418b5854bf515cfdd5220'
params = {
	'appkey': 'c4ee7256953eb3b8ff44ecf6b2de38d80adeb299',
	'token': '!*177UCSXtEBwQUqMEPdYItCwtXqlROO@q0erG3cTJc@g*-',
	'format': 'json'
}
domain = 'http://new.udh.yonyouup.com/'


def getSign(params):
	try:
		paramsList = sorted(params.items(), key=lambda item: item[0])
		sign = reduce(lambda x, y: x + y[0] + y[1], paramsList, '')
		sign = secret + sign + secret
		sign = md5(sign.encode())
		return sign.upper()
	except Exception as e:
		print(e)
		raise


def setValueNone(jsonObj):
	if isinstance(jsonObj,list):
		for index,x in enumerate(jsonObj):
			if isinstance(x,(list,dict)):
				setValueNone(x)
			else:
				jsonObj[index]=None
	elif isinstance(jsonObj,dict):
		for k,v in jsonObj.items():
			if isinstance(v,(list,dict)):
				setValueNone(v)
			else:
				jsonObj[k]=None




if __name__ == '__main__':
	# sign=getSign(params)
	# url='/rs/Orders/getSummaryOrders'
	# url=pathJoin(domain,url)
	# params['sign']=sign
	# pprint.pprint(params)
	# r=requests.get(url,params=params)
	# print(r.status_code)
	# res=json.loads(r.text)
	# pprint.pprint(res)

	expectData='''
	{
 'code':200,
 'data': {'count': 24,
          'data': [{'cOrderNo': 'UO7f4-32521606070006',
                    'cPayStatusCode': 'PARTPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-06-07 16:01:48',
                    'fPayMoney': 3000.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521606140002',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-06-14 15:39:15',
                    'fPayMoney': 500.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521606150003',
                    'cPayStatusCode': 'NOTPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-06-15 13:58:16',
                    'fPayMoney': 2000.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521606160001',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-06-16 10:36:22',
                    'fPayMoney': 20000.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521606160003',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-06-16 11:18:10',
                    'fPayMoney': 20000.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32591606160004',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小八',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-06-16 13:42:38',
                    'fPayMoney': 900.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521606160007',
                    'cPayStatusCode': 'CONFIRMPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-06-16 20:44:37',
                    'fPayMoney': 500.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521606160010',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小受',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-06-16 21:16:00',
                    'fPayMoney': 100.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521606200001',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-06-20 14:46:00',
                    'fPayMoney': 2000.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607190001',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小八',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-19 10:54:52',
                    'fPayMoney': 900.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607190003',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-19 11:03:07',
                    'fPayMoney': 4900.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607190004',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-19 11:06:54',
                    'fPayMoney': 5200.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607190007',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'CONFIRMORDER',
                    'dOrderDate': '2016-07-19 14:40:07',
                    'fPayMoney': 0.01,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607190008',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'CONFIRMORDER',
                    'dOrderDate': '2016-07-19 14:53:44',
                    'fPayMoney': 0.01,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607190009',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-19 16:00:50',
                    'fPayMoney': 0.01,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607200001',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'DELIVERGOODS',
                    'dOrderDate': '2016-07-20 09:44:45',
                    'fPayMoney': 4900.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607200002',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-20 09:44:53',
                    'fPayMoney': 4900.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607200003',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-20 09:45:03',
                    'fPayMoney': 4900.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607200004',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-20 09:45:12',
                    'fPayMoney': 4900.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607200005',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-20 09:45:20',
                    'fPayMoney': 4900.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607200006',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-20 09:45:27',
                    'fPayMoney': 4900.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607200007',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-20 10:11:06',
                    'fPayMoney': 5000.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607200008',
                    'cPayStatusCode': 'FINISHPAYMENT',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-20 14:15:25',
                    'fPayMoney': 960.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'},
                   {'cOrderNo': 'UO7f4-32521607210002',
                    'cPayStatusCode': 'CONFIRMPAYMENT_ALL',
                    'cReceiveContacter': '小一',
                    'cStatusCode': 'ENDORDER',
                    'dOrderDate': '2016-07-21 09:46:42',
                    'fPayMoney': 1500.0,
                    'iAgentId': 8091,
                    'iCorpId': 2036,
                    'pubuts': '2016-09-18 13:24:25'}]}}
	'''.replace("'", "\"")
	expectJson=json.loads(expectData)
	# setValueNone(expectJson)
	# pprint.pprint(expectJson)
	# print(expectJson==expectJson1)

	# print(expectJson)
	params = '{\'format\': \'json\'}'.replace("'", "\"")
	UOrder=impClass(projectClass['udh'])
	udh=UOrder(params)
	params=udh.getFullRequestData()
	url = udh.getFullUrl('/rs/Orders/getSummaryOrders')
	r = requests.get(url, params=params)
	# print(r.status_code)
	res=json.loads(r.text)
	# setValueNone(res)
	# pprint.pprint(res)
	# print(res==expectJson)
	# print(udh.compareJson(res,expectJson))

	a=udh.compareFormat(expectJson,res,False)
	print(a)