# 题目：打印出杨辉三角形（要求打印出10行如下图）。　　

 # 1
# 1  1
# 1 2 1
#  1 3 3 1

class YangHui():
	def __init__(self,lineNumber):
		self.lineNumber=lineNumber
		self.lastLine=[]

	def getCurrentLine(self,number):
		if number==1:
			line=[1]
		elif number==2:
			line=[1,1]
		else:
			line=[1,1]
			l=len(self.lastLine)
			for x in range(l-1):
				line.insert(x+1,self.lastLine[x]+self.lastLine[x+1])
		self.lastLine=line
		return line

	def __iter__(self):
		for x in range(1,self.lineNumber+1):
			yield self.getCurrentLine(x)


for x in YangHui(100):
	print(x)
