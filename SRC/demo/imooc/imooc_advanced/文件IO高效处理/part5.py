# 如何访问文件的状态
# 文件的类型
# 文件的访问权限
# 文件的最后访问 修改 节点状态更改时间
# 普通文件的大小
#
# 方法一： 标准库中os模块下的三个系统调用stat,fstat,lstat获取文件状态
# os.stat 不取符号链接
# os.lstat 取符号链接
# os.fstat 需要一个打开的文件描述符
# open().fileno() #获取文件描述符
import os, stat,time

s = os.stat('demo.txt')
print(s.st_mode)
print(bin(s.st_mode))
print(stat.S_ISDIR(s.st_mode))  # 判断状态
print(stat.S_ISREG(s.st_mode))

# 获取文件权限
res=s.st_mode & stat.S_IRUSR  #判断标志位  大于0就是真的
print(res)

#获取文件访问时间
print(time.localtime(s.st_atime))

#获取文件大小
res=s.st_size
print(res)

# 方法二：标准库中os.path下的一些函数
res=os.path.isdir('x.txt')
print(res)

res=os.path.islink('x.txt')
print(res)



