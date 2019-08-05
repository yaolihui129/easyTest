# 如何在线程间进行事件通知

# 实现一个线程，将转换出的xml文件压缩打包，比如转换线程每生产出100个xml文件，
# 就通知打包线程将他们打包成一个XXX.tgz文件，并删除xml文件，
# 打包完成后，打包线程反过来通知转换线程，转换线程继续转换

# 线程间的事件通知，可以使用标准库中Threanding,Event
# 1：等待事件一端调用wait，等待事件
# 2：通知事件一端调用set，通知事件


import tarfile
import os
# def tarXML(tfname):
# 	tf=tarfile.open(tfname,'w:gz')
# 	for fname in os.listdir('.'):
# 		if fname.endswith('.xml'):
# 			tf.add(fname)
# 			os.remove(fname)
# 	tf.close()
#
# 	if not tf.members:
# 		os.remove(tfname)
# tarXML('test.tgz')



import csv

from io import StringIO
from xml.etree.ElementTree import Element, ElementTree

import requests

from threading import Thread, Event
from queue import Queue


# def f(e):
# 	print('f 0')
# 	e.wait()
# 	print('f 1')
#
#
# e = Event()
# t = Thread(target=f, args=(e,))
# t.start()
# e.set()  # 解除阻塞
# e.clear()  # 清理掉


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
		print('Download', self.sid)
		data = self.download(self.url)
		# 2.sid,data传递给conver线程
		# lock
		self.queue.put((self.sid, data))


class ConvertThread(Thread):
	def __init__(self, queue, cEvent, tEvent):
		Thread.__init__(self)
		self.queue = queue
		self.cEvent = cEvent
		self.tEvent = tEvent

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
		count = 0
		while True:
			# 1.sid data
			sid, data = self.queue.get()
			print('Covert', sid)
			if sid == -1:
				self.cEvent.set()
				self.tEvent.wait()
				break
			if data:
				fname = str(sid).rjust(6, '0') + '.xml'
				with open(fname, 'wb') as wf:
					self.csvToXml(data, wf)
				count += 1
				if count == 5:
					self.cEvent.set()
					self.tEvent.wait()
					self.tEvent.clear()
					count = 0


class TarThread(Thread):
	def __init__(self, cEvent, tEvent):
		Thread.__init__(self)
		self.count = 0
		self.cEvent = cEvent
		self.tEvent = tEvent
		self.setDaemon(True)  # 设置为守护进程

	def tarXML(self):
		self.count += 1
		tfname = '%d.tgz' % self.count
		tf = tarfile.open(tfname, 'w:gz')
		for fname in os.listdir('.'):
			if fname.endswith('.xml'):
				tf.add(fname)
				os.remove(fname)
		tf.close()

		if not tf.members:
			os.remove(tfname)

	def run(self):
		while True:
			self.cEvent.wait()
			self.tarXML()
			self.cEvent.clear()

			self.tEvent.set()

if __name__ == '__main__':
	q = Queue()
	dThreads = [DownloadThread(i, q) for i in range(1, 12)]

	cEvent = Event()
	tEvent = Event()

	cThread = ConvertThread(q, cEvent, tEvent)
	tThread = TarThread(cEvent, tEvent)
	tThread.start()
	for t in dThreads:
		t.start()
	cThread.start()

	for t in dThreads:
		t.join()

	q.put((-1, None))
