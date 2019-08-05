# 如何对字符串进行左右居中对齐？

# 方法一：使用字符串的str.ljust(),str.rjust(),str.center()进行左右居中对齐
# 方法二：使用format()方法，传递类似'<20','>20','^20'参数完成同样任务

# 方法一：
s='abc'
print(s.ljust(10,'|'))
print(s.rjust(10,'='))
print(s.center(10,'='))


# 方法二：
res=format(s,'<20')
print(res)
res=format(s,'>20')
print(res)
res=format(s,'^20')
print(res)

#小例子
testCase = {
	'runType': 'Remote',  # 运行模式(Remote,Browser)
	'xmlDir': 'script/config/',  # 测试方案配置文件夹路径(支持绝对路径)
	'testCaseDir': 'script/testCase/',  # 测试用例配置文件夹路径(必须相对于项目根目录)
	'filesDir': 'script/files/',  # 待上传文件路径
}
maxLength=max(map(len,testCase.keys()))
print(maxLength)
for k,v in testCase.items():
	print(k.ljust(maxLength),':',v)