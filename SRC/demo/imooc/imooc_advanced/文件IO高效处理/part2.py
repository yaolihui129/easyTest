# 如何处理二进制文件

import struct
# res=struct.unpack('h',b'\x01\x02')
# print(res)

import array

f=open('demo.wav','rb')
f.seek(0,2) #指针指向末尾
# print(f.tell())
n =(f.tell()-44)//2
buf =array.array('h',(0 for _ in range(n)))
f.seek(44)
f.readinto(buf)
print(buf[10])