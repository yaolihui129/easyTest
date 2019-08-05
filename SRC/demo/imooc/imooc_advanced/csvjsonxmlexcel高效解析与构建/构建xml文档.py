# csv转换成xml
# 使用标准库中的xml.etree.ElementTree 构建ElementTree，使用write方法写入文件
import csv
from xml.etree.ElementTree import Element, ElementTree

element=Element('Data') #tag名字
print(element.tag)

element.set('name','abc') #设置属性
element.text='123' #设置内容
from xml.etree.ElementTree import tostring
print(tostring(element)) #查看xml结构

e2=Element('Row')
e3=Element('Open')
e3.text='8.80'

e2.append(e3) #添加子元素
print(tostring(e2))

print(tostring(e2))
tostring(e2)

e2.text=None
element.append(e2)
print(tostring(element))

et=ElementTree(element) #创建tree
et.write('demo.xml') #写入xml

def csvToXml(fname):
	with open(fname,'r') as f:
		reader=csv.reader(f)
		headers=reader.__next__()
		headers=list(map(lambda x:x.replace(' ',''),headers))
		root =Element('Data')
		for i,row in enumerate(reader) :
			if i>10:
				break
			eRow=Element('Row')
			root.append(eRow)
			for tag,text in zip(headers,row): #同时迭代两个序列
				e=Element(tag)
				e.text=text
				eRow.append(e)
	return ElementTree(root)


if __name__ == '__main__':
	et =csvToXml('pingan.csv')
	et.write('pingan.xml')


