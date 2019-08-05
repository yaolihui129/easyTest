# coding: utf-8
'''
z = zipfile.ZipFile('') , extractall
z.extractall(pwd)
'''
import zipfile
import threading
import itertools

def zipbp(zfile, pwd):
	try:
		zfile.extractall(pwd=pwd)
		print('password found : %s' % pwd)
		open('result.txt','a').write('password found : %s' % pwd)
	except Exception as e:
		return


def main(file,dictFile=None):
	zfile = zipfile.ZipFile(file)
	pwdall = open(dictFile)
	for pwda in pwdall.readlines():
		pwd = pwda.strip('\n').encode('ascii')
		t = threading.Thread(target=zipbp, args=(zfile, pwd))
		t.start()
		t.join()

def main1(file,words,repeat=6):
	zfile = zipfile.ZipFile(file)
	for pwda in getDict(words,repeat):
		pwd = pwda.strip('\n').encode('ascii')
		print(pwd)
		t = threading.Thread(target=zipbp, args=(zfile, pwd))
		t.start()
		t.join()


def getDict(words,repeat=6):
	r=itertools.product(words,repeat=repeat)
	for i in r:
		# print("".join(i))
		yield  "".join(i)

if __name__ == '__main__':
	words1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	words2="abcdefghijklmnopqrstuvwxyz"
	words3="1234567890"
	# main('a.zip','dict.txt')
	# getDict(words3,6)
	for x in range(1,10):
		print('解密开始:')
		print('words=%s'%(words1))
		main1('key.zip',words1,x)
		print('%d位完毕'%(x))