'''
1.URL Parameters:URL参数
方便，限制长度
requests.get(url,params=s{'key1':'value1','key2':'value2'})
注意是params

2.表单参数提交
Content-Type:application/x-www-form-urlencoded
内容： key1=value1&key2=value2
requests.post(url,data={'key1':'value1','key2':'value2'})
注意是data

3.json参数提交
Content-Type:application/json
内容: '{"key1":"value1","key2":"value2"}'
requests.post(url,json={'key1':'value1','key2':'value2'})
注意是json

4.patch

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
	print(better_print(response.text))

def params_request():
	response=requests.get(build_uri('users'),params={'since':11})
	print(better_print(response.text))
	print(response.request.headers)
	print(response.url)


def json_request():
	response=requests.patch(build_uri('user'),auth=('imoocdemo','imoocdemo123'),json={'name':'testmooc2','email':'hello-world@imooc.org'})
	print(better_print(response.text))
	print(response.request.headers)
	print(response.request.body)
	print(response.status_code)

if __name__=='__main__':
	# request_method()
	# params_request()
	json_request()