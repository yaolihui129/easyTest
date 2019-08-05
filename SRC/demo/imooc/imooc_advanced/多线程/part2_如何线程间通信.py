# 如何线程间通信

# 实际案例：
# 由于全局解释器锁的存在，多线程进行cpu密集型操作并不能提高执行效率
# 我们修改程序构架：
# 1.使用多个DownloadThread线程进行下载(i/o操作)
# 2.使用一个ConverThread线程进行转换(cpu密集型操作)
# 3.下载线程把下载数据安全地传递给转换线程

# 使用标准库中Queue.Queue,它是一个线程安全的队列
# Download线程把下载数据放入队列，Convert线程从队列里提取数据

import csv

from io import StringIO
from xml.etree.ElementTree import Element, ElementTree

import requests

from threading import Thread
from queue import Queue


class DownloadThread(Thread):
	def __init__(self, sid, queue):
		Thread.__init__(self)
		self.sid = sid
		self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
		self.url %= str(sid).rjust(6, '0')
		self.queue = queue

	def download(self, url):
		response = requests.get(url, timeout=3)
		if response.ok:
			return StringIO(response.text)  # 支持文件操作的内存对象

	def run(self):
		# 1.下载
		print('Download',self.sid)
		data = self.download(self.url)
		# 2.sid,data传递给conver线程
		# lock
		self.queue.put((self.sid, data))


class ConvertThread(Thread):
	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue

	def csvToXml(self, scsv, fxml):
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
		root = self.indent(root)
		et = ElementTree(root)
		et.write(fxml)

	def indent(self, elem, level=0):
		i = "\n" + level * "  "
		if len(elem):
			if not elem.text or not elem.text.strip():
				elem.text = i + "  "
			for e in elem:
				self.indent(e, level + 1)
			if not e.tail or not e.tail.strip():
				e.tail = i
		if level and (not elem.tail or not elem.tail.strip()):
			elem.tail = i
		return elem

	def run(self):
		while True:
			# 1.sid data
			sid, data = self.queue.get()
			print('Covert',sid)
			if sid == -1:
				break
			if data:
				fname = str(sid).rjust(6, '0') + '.xml'
				with open(fname, 'wb') as wf:
					self.csvToXml(data, wf)


q = Queue()
dThreads = [DownloadThread(i, q) for i in range(1, 12)]
cThread = ConvertThread(q)
for t in dThreads:
	t.start()
cThread.start()

for t in dThreads:
	t.join()

q.put((-1, None))
