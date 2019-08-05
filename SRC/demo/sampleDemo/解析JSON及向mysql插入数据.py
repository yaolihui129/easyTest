import json
import pymysql
import sys

#传参格式：
# {'db':{'host':'localhost','user':'root','passwd':'root','db':'test','charset':'utf8','tablename':'test1'},'files':['partJson.json']}

DB={
	'host':'localhost',
	'user':'root',
	'passwd':'root',
	'db':'test',
	'charset':'utf8',
	'tablename':'test1'
}

FILES=['partJson.json']

def connDB():  # 连接数据库函数
	conn = pymysql.connect(host=DB['host'], user=DB['user'], passwd=DB['passwd'], db=DB['db'], charset=DB['charset'])
	cur = conn.cursor()
	return (conn, cur)

def exeUpdate(cur, sql):  # 更新语句，可执行update,insert语句
	sta = cur.execute(sql)
	return (sta)

def connClose(conn, cur):  # 关闭所有连接
	cur.close()
	conn.close()

def readFile(path):#读取json文件
	file = open(path)
	temp = []
	while 1:
		lines = file.readlines(100000)
		if not lines:
			break
		for line in lines:
			try:
				line=line.strip()
				res=json.loads(line)
				temp.append(res)
			except Exception as e:
				print(e)
				raise
	return temp


def doSomething(dataList):
	# 调用连接数据库的函数
	conn, cur = connDB()
	try:
		for res in dataList:
			sql="insert into %s values('%s','%s','%s',%s)"%(DB['tablename'],res['d'],res['_c3'],res['_c9'],res['c'])
			sta = exeUpdate(cur, sql)
			if (sta == 1):
				print('插入成功')
			else:
				print('插入失败:%s'%(res))
	except Exception as e:
		print(e)
	finally:
		connClose(conn, cur)

def init(str):
	decodeJson = json.loads(str.replace('\'','\"'))
	DB['host']=decodeJson['db']['host']
	DB['user']=decodeJson['db']['user']
	DB['passwd'] = decodeJson['db']['passwd']
	DB['db'] = decodeJson['db']['db']
	DB['charset'] = decodeJson['db']['charset']
	DB['tablename']=decodeJson['db']['tablename']
	FILES=[]
	FILES.append(decodeJson['files'])


if __name__=='__main__':
	if len(sys.argv) >=2:
		init(sys.argv[1])
	for x in FILES:
		dataList=readFile(x)
		doSomething(dataList)
