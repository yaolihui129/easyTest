
import os
import random
import time
from threading import current_thread
import datetime as dt

from SRC.common.loga import putSystemLog


def getCurrentTime():
	'''
	获取当前时间
	:return:
	'''
	return dt.datetime.now().strftime('%Y%m%d%H%M%S%f')


def getLogName():
	'''
	获取一个当前线程的随机日志名称
	:return:
	'''
	now = dt.datetime.now().strftime('%Y%m%d_%H_%M_%S_%f')
	threadId = current_thread().ident

	return "%s_%sreport.log" % (now, threadId)


# 获取图片保存路径
def getImageSavePath(dir):
	now = dt.datetime.now().strftime('%Y%m%d_%H_%M_%S_%f')
	threadId = current_thread().ident
	# browserName=current_thread()._args[0]
	return os.path.join(dir, '%s_%simage.jpg' % (now, threadId)).replace('\\', '/')


def createDir(dir, addDateDir=True):
	dirPath = dir
	if addDateDir:
		date = time.strftime('%Y%m%d', time.localtime())
		dirPath = os.path.join(dir, date)
	time.sleep(random.uniform(0, 1))  # 延迟等待0-1秒
	try:
		if not os.path.exists(dirPath):
			os.makedirs(dirPath)
	except Exception as e:
		putSystemLog('[ERROR-0004-0]:创建日志目录失败引发的异常.%s' % e, None, False, '', '', True)
	return dirPath


def choose(bool, a, b):
	return (bool and [a] or [b])[0]


def md5(str):
	'''
	返回字符串的md5
	:param str:
	:return:
	'''
	import hashlib
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

def impClass(classPath):
	'''
	动态导入指定的类
	:param classPath:
	:return:
	'''
	if not classPath:
		return
	temp=classPath.split('.')
	className=temp[-1]
	modulePath='.'.join(temp[:-1])
	from importlib import import_module
	model_module = import_module(modulePath)  # 引入模块
	return getattr(model_module,className)


def isAbsoluteUrl(url):
	res=False
	if isinstance(url,str):
		u = url.lower()
		if u.startswith('http:') or u.startswith('https:'):
			res=True
	return res
