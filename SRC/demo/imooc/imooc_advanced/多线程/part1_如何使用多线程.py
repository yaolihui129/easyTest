# 9如何使用多线程
# 实际案例：
# 通过雅虎网站获取了中国股市某只股票csv数据文件，
# 现在要下载多只股票的csv数据，并将其转换为xml文件

# 如何使用多线程来提高下载并处理的效率
# 使用标准库threading.Thread创建线程，在每一个线程中下载并转换一只股票数据

#全局解释器 不能实现真正的并发 GIL python中的线程只适合处理io操作

# http://table.finance.yahoo.com/table.csv?s=000001.sz
import csv
from io import StringIO
from xml.etree.ElementTree import Element, ElementTree

import requests


def download(url):
	response = requests.get(url, timeout=3)
	if response.ok:
		return StringIO(response.text)  # 支持文件操作的内存对象


def csvToXml(scsv, fxml):
	reader = csv.reader(scsv)
	headers = reader.__next__()
	headers = list(map(lambda h: h.replace(' ', ''), headers))

	root = Element('Data')
	for row in reader:
		eRow = Element('Row')
		root.append(eRow)
		for tag, text in zip(headers, row):
			e = Element(tag)
			e.text = text
			eRow.append(e)
	root = indent(root)
	et = ElementTree(root)
	et.write(fxml)


def indent(elem, level=0):
	i = "\n" + level * "  "
	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + "  "
		for e in elem:
			indent(e, level + 1)
		if not e.tail or not e.tail.strip():
			e.tail = i
	if level and (not elem.tail or not elem.tail.strip()):
		elem.tail = i
	return elem


def handle(sid):
	print('Download...(%d)' % sid)
	url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
	url %= str(sid).rjust(6, '0')
	rf = download(url)
	if rf is None: return

	print('Convert to xml...(%d)' % sid)
	fname = str(sid).rjust(6, '0') + '.xml'
	with open(fname, 'wb') as wf:
		csvToXml(rf, wf)


from threading import Thread


# 方法一
# t=Thread(target=handle,args=(1,))
# t.start()

# 方法二
class MyThread(Thread):
	def __init__(self, sid):
		Thread.__init__(self)
		self.sid = sid

	def run(self):
		handle(self.sid)


# t=MyThread(1)
# t.start()
# t.join() #阻塞函数

threads = []
for i in range(1, 11):
	t = MyThread(i)
	threads.append(t)
	t.start()

for t in threads:
	t.join()
print('main thread')



# if __name__ == '__main__':
# url='http://table.finance.yahoo.com/table.csv?s=000001.sz'
# rf=download(url)
# if rf:
# 	with open('000001.xml','wb') as wf:
# 		csvToXml(rf,wf)

# for sid in range(1, 11):
# 	print('Downliad...(%d)' % sid)
# 	url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
# 	url %= str(sid).rjust(6, '0')
# 	rf=download(url)
# 	if rf is None:continue
#
# 	print('Convert to xml...(%d)'%sid)
# 	fname=str(sid).rjust(6,'0')+'.xml'
# 	with open(fname,'wb') as wf:
# 		csvToXml(rf,wf)
