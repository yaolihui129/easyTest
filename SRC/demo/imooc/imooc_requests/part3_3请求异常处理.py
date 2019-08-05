import requests
import json

URL = 'https://api.github.com'


def build_uri(endpoint):
	return '/'.join([URL, endpoint])


def better_print(json_str):
	return json.dumps(json.loads(json_str), indent=4)


def request_method():
	response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'))
	print(better_print(response.text))


def params_request():
	response = requests.get(build_uri('users'), params={'since': 11})
	print(better_print(response.text))
	print(response.request.headers)
	print(response.url)


def timeout_request():
	try:
		response = requests.get(build_uri('user/emails'),timeout=10)
	except requests.exceptions.Timeout as e:
		print(e)
	except requests.exceptions.HTTPError as e:
		print(e)
	else:
		print(response.text)
		print(response.status_code)

if __name__=='__main__':
	timeout_request()