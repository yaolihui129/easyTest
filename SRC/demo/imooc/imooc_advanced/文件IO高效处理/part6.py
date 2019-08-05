# 如何使用临时文件

#使用标准库中tempfile下的TemporaryFile，NamedTemporaryFile
# NamedTemporaryFile 创建一个带名字的

from tempfile import TemporaryFile,NamedTemporaryFile
# f=TemporaryFile()
# f.write('abcdef'*100000)
# f.seek(0)
# f.read(100)


ntf=NamedTemporaryFile(delete=False)
print(ntf.name)
i=1