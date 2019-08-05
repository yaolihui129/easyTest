'''
http://github.com

请求方法
GET： 查看资源
POST： 增加资源
PUT：修改资源
DELETE:删除资源

HEAD：查看响应头（就相当于GET，去掉相应内容）
OPTIONS：查看可用请求方法



'''
import json

import requests

URL='https://api.github.com'

def build_uri(endpoint):
	return '/'.join([URL,endpoint])

def better_print(json_str):
	return json.dumps(json.loads(json_str),indent=4)

def request_method():
	response=requests.get(build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'))
	# print(response.text)
	print(better_print(response.text))

if __name__=='__main__':
	request_method()