
author='Kenneth Reitz'
author_bolg='www.kennethreitz.org'
request_doc='http://docs.python-requests.org/en/master/'

description='''
1.爬虫必备法器
2.服务器变成基础（Restful API）
3.自动化测试工具（接口测试）
'''

env='''
1.Python
2.pip
3.virtualenv
4.Requests2.11
5.httpbin
'''

pip='''
pip install virtualenv
pip install requests
pip freeze
'''

virtualenv='''
1.创建虚拟目录
virtualenv .env
2.激活env(windows好像不是这么激活的)
source .env/bin/activate
'''

httpbin='''
服务器：一个testing services
http://httpbin.org
安装
pip install gunicorn httpbin
启动
gunicorn httpbin:app

'''