import os
import sys
# zipfile是Python标准库
import zipfile

# 尝试导入扩展库unrar，如果没有就临时安装
try:
	from unrar import rarfile
except:
	path = '"' + os.path.dirname(sys.executable) + '\\scripts\\pip" install --upgrade pip'
	os.system(path)
	path = '"' + os.path.dirname(sys.executable) + '\\scripts\\pip" install unrar'
	os.system(path)
	from unrar import rarfile


def getFileStream(filename):
	if filename.endswith('.zip'):
		fp = zipfile.ZipFile(filename)
	elif filename.endswith('.rar'):
		fp = rarfile.RarFile(filename)
	else:
		fp = None
	return fp


def mkDir(desPath):  # 解压缩的目标文件夹
	if not os.path.exists(desPath):
		os.mkdir(desPath)


def checkNoPwd(fp, desPath):
	fp.extractall(desPath)
	fp.close()
	print('No password')


def checkPwd(fp, desPath):
	try:
		fpPwd = open('pwddict.txt')
	except:
		print('No dict file pwddict.txt in current directory.')
		return
	for pwd in fpPwd:
		pwd = pwd.rstrip()
		try:
			if filename.endswith('.zip'):
				for file in fp.namelist():
					# 对zip文件需要重新编码再解码，避免中文乱码
					fp.extract(file, path=desPath, pwd=pwd.encode())
					os.rename(desPath + '\\' + file, desPath + '\\' + file.encode('cp437').decode('gbk'))
				print('Success! ====>' + pwd)
				fp.close()
				break
			elif filename.endswith('.rar'):
				fp.extractall(path=desPath, pwd=pwd)
				print('Success! ====>' + pwd)
				fp.close()
				break
		except:
			pass
	fpPwd.close()


def decryptRarZipFile(filename,dictType='file'):
	# 根据文件扩展名，使用不同的库
	fp = getFileStream(filename)
	desPath = filename[:-4]
	mkDir(desPath)
	try:  # 先尝试不用密码解压缩，如果成功则表示压缩文件没有密码
		checkNoPwd(fp, desPath)
		return
	except:  # 使用密码字典进行暴力破解
		checkPwd(fp, desPath)


if __name__ == '__main__':

	filename = sys.argv[1]
	if os.path.isfile(filename) and filename.endswith(('.zip', '.rar')):
		decryptRarZipFile(filename)
	else:
		print('Must be Rar or Zip file')
