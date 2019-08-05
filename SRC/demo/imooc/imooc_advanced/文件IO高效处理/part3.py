# 如何设置文件的缓冲
# f=open('demo.txt','w')
#
# f.write('abc')
#
# f.write('+'*4093)
#
# f.write('-')

#文件io操作需要使用缓冲区，有足够多的数据才进行系统调用，文件的缓冲行为

#全缓冲 open函数的buffering 设置为大于1的整数n，n为缓冲区大小

#行缓冲 open函数的buffering 设置为1

#无缓冲 open函数的buffering 设置为0

f=open('demo2.txt','w',buffering=2048)

f.write('+'*1024)
f.write('+'*1023)
f.write('-'*2)

f=open('demo3.txt','w',buffering=1)

f.write('+'*1024)
f.write('+'*1023)
f.write('-'*2)