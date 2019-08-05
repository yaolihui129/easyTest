# zhangfjb@yonyou.com 111111
# import requests
# auth=('zhangfjb@yonyou.com', '111111')
# url=r'http://10.1.197.134:8088/sys/osetting'
# datas={'osdisplay':1}
# cookies = dict(_token='DwRVbSKbiqMUOIvumXdw7fuetYzAyuR1Y6SxHlrR')
# r=requests.post(url,data=datas,cookies=cookies)
# print(r.status_code)
# print(r.text)
# print('\n')
# print(r.headers)
import requests

url='http://httpbin.org/ip'
datas=None
r=requests.get(url,data=datas)
print(r.status_code)
print(r.text)
print('\n')
print(r.headers)