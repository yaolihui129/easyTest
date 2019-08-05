
'''
urllib介绍
1.urllib和urllib2是相互独立的模块
2.requests库使用了urllib3（多场请求重复使用一个socket）
'''

# # bytes object
# b = b"example"
#
# # str object
# s = "example"
#
# # str to bytes
# bytes(s, encoding = "utf8")
#
# # bytes to str
# str(b, encoding = "utf-8")
#
# # an alternative method
# # str to bytes
# str.encode(s)
#
# # bytes to str
# bytes.decode(b)
from urllib.parse import urlencode
from urllib.request import urlopen

URL_IP='http://httpbin.org/ip'
URL_GET='http://httpbin.org/get'
def use_simple_urllib():
	response=urlopen(URL_IP)
	print('>>>Response Headers:')
	print(response.info())

	print('>>>Response Body：')
	print(''.join([bytes.decode(line) for line in response.readlines()]))

def use_params_urllib():
	#构建请求参数
	params=urlencode({'param1':'Hello','param2':'world'})
	print('Request Params:')
	print(params)
	#发送请求
	response=urlopen('?'.join([URL_GET,'%s'])%params)
	print('>>>Response Headers:')
	print(response.info())
	print('>>>Status Code:')
	print(response.getcode())
	print('>>>Response Body：')
	print(''.join([bytes.decode(line) for line in response.readlines()]))

if __name__=='__main__':
	print('>>>Use simple urllib:')
	use_simple_urllib()
	print()
	print('>>>Use params urllib:')
	use_params_urllib()


