# for x in range(1,2):
# 	print(x)

# a=['a','b','c']
# print(','.join(a))

#
#
# a='1,2,3'
# aa=['1','2','3','4','5']
# b=a.split(',')
# c=set(b)
# print(c)
# cc=[x for x in c if x not in aa]
# print(cc)

# name=input('what?')
# print(name+'abc')
# from selenium import webdriver
#
# driver = webdriver.Remote("http://10.10.12.103:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNITWITHJS)
# driver.get('http://www.baidu.com')
# i = 1

from selenium.webdriver import Remote
dc = {
	'browserName': 'htmlunit'
}
driver=Remote(command_executor='http://10.10.12.103:4444/wd/hub',desired_capabilities=dc)
driver.get('http://www.baidu.com')
i=12