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

import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'


def use_simple_requests():
	response = requests.get(URL_IP)
	print('>>>Response Headers:')
	print(response.headers)

	print('>>>Response Body：')
	print(response.text)


def use_params_requests():
	# 构建请求参数
	params = {'param1': 'Hello', 'param2': 'world'}
	# 发送请求
	response = requests.get(URL_IP, params)
	print('>>>Response Headers:')
	print(response.headers)
	print('>>>Status Code:')
	print(response.status_code)
	print(response.reason)
	print('>>>Response Body：')
	print(response.json())


if __name__ == '__main__':
	print('>>>Use simple requests:')
	use_simple_requests()
	print()
	print('>>>Use params requests:')
	use_params_requests()
