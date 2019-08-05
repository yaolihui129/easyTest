# 使用标准库中xml.etree.ElementTree

from xml.etree.ElementTree import parse

f = open('demo.xml')
et = parse(f)
root = et.getroot()

# root.tag
# root.attrib 字典
# root.text strip()

# root.getchildren()  #获取子元素 不推荐
for child in root:
	print(child.get('name'))

# root.find  找到第一个
# root.findall 找到所有的
# root.iterfind('country') 生成器对象 用于迭代
#以上三种方法只能查找直接子元素

# root.iter() #列出所有元素节点 返回一个列表
# root.iter('rank') #递归查找标签是rank的子节点

#高级用法
# root.findall('country/*')
# root.findall('.//rank') 无论在哪个层次中
# root.findall('.//rank/..') 查找rank的父级

# root.findall('country[@name]')
# root.findall('country[@name="Singa"]')
# root.findall('country[",rank]')
# root.findall('country[2]')
# root.findall('country[last()]')
# root.findall('country[last()-1]')

