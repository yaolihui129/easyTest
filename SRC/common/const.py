# coding=utf-8


BROWSER_ID = ['ff', 'ch', 'ie']  # 浏览器简称 火狐，谷歌，ie

FINDELEMENT_TYPE = ['findAssert']  # 查找断言

INTERFACE_PARAMS = {
	'mustContain': ['projectClass',  # 项目名称简写
					'url',  # 待测试接口，可以为相对路径
					'method',  # 请求方式
					'dataType',  # 请求数据类型
					'expectType'  # 预期返回类型
					],  # 接口测试参数文件中必须拥有的id字段，如果没有，则会抛出异常
	'contain': ['data',  # 请求的数据参数
				'expect',  # 预期返回的数据
				'resultCompare',  # 结果比较
				],  # 接口测试参数化文件中的字段：可以包含，也可以不包含，如果没有，参数类中赋值为空
	'dataType': ['json',  # 请求数据类型种类
				 ],  # 支持的请求类型
	'method': ['get',
			   'post'
			   ],  # 支持的请求方法
	'expectType': ['string',
				   'json',
				   'xml'],  # 支持的返回数据格式
	'resultCompare': {'0':'不比较',  # 不比较
					  '1':'比较key',  # 比较key
					  '2':'比较format',  # 比较format
					  '3':'比较value',  # 比较value
					  '4':'完全对比',  # 完全对比
					  },
}


class Agent():
	'''
	浏览器类型
	'''
	REMOTE = "Remote"
	IE = "Internet Explorer"
	CHROME = "Google Chrome"
	FIREFOX = "Mozilla Firefox"


class RunResult():
	'''
	运行结果
	'''
	PASS = "PASS"
	FAIL = "FAIL"
	ERROR = "ERROR"
	TRUE = "TRUE"  # 发送数据时转换为PASS
	FALSE = "FALSE"  # 发送数据时转换为PASS
	WARNING = "WARNING"  # 警告


class RunType():
	'''
	运行类型
	'''
	REMOTE = "remote"  # 远程服务器启动
	BROWSER = "browser"  # 本地浏览器启动


class RunModel():
	'''
	运行模式
	'''
	NORMAL = "NORMAL"  # 正常模式
	ONLINE = "ONLINE"  # 线上模式
	TESTING = "TESTING"  # 测试模式


class TestType():
	'''
	测试类型
	'''
	UI = "UI"  # ui自动化测试
	INTERFACE = "INTERFACE"  # 接口自动化测试


class RunStatus():
	'''
	运行状态
	'''
	START = 'START'  # 启动
	RUNNING = 'RUNNING'  # 运行中
	END = 'END'  # 结束
	BEGANSTART = 'BEGANSTART'  # 启动之前


class RequestMethod():
	'''
	请求方式
	'''
	GET = 'GET'
	POST = 'POST'


class RequestDataType():
	'''
	请求数据类型
	'''
	STRING = 'STRING'
	JSON = 'JSON'
