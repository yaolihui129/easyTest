'''
Session
		PreparedRequest
						Response


'''
import json

URL = 'https://api.github.com'


def build_uri(endpoint):
	return '/'.join([URL, endpoint])


def better_print(json_str):
	return json.dumps(json.loads(json_str), indent=4)


def hard_requests():
	from requests import Request, Session
	s = Session()
	headers = {'User-Agent': 'fake1.3.4'}
	req = Request('GET', build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'), headers=headers)
	prepped = req.prepare()
	print(prepped.body)
	print(prepped.headers)

	resp=s.send(prepped,timeout=5)
	print(resp.status_code)
	print(resp.request.headers)
	print(resp.text)

if __name__=='__main__':
	hard_requests()