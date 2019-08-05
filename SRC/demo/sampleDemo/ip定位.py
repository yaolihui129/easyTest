# -*- coding: utf-8 -*- 
""" 
Created on Wed Oct 12 12:40:24 2016 
@author: Administrator
"""
import requests
import json

ak = 'sfdzPqrU8xYevtmZGEhyfQoPQwePIvr5'
ip = '123.103.9.9'
URL = 'http://api.map.baidu.com/highacciploc/v1?qcip=%s&qterm=pc&ak=%s&coord=bd09ll&extensions=1' % (ip, ak)


def get_html(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1581.2 Safari/537.36'}
	text = requests.get(url, headers=headers).text
	return text


def formated_html(text):
	jo = json.loads(text)  # 或者直接用eval函数将text转成dict
	business = jo['content']['business']
	for k, v in jo['content']['address_component'].items():
		print(k, ':', v)
	print('formatted_address', ':', jo['content']['formatted_address'])
	print('business', ':', jo['content']['business'])
	print('location', ':', jo['content']['location'])


if __name__ == '__main__':
	text = get_html(URL)
	formated_html(text)
