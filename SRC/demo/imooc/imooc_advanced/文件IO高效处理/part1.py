#如何读写文本文件

s='你好'
res=s.encode('utf-8')
print(res)

res=s.encode('gbk')
print(res)

#python3 字节字符串 b''
#t 指定文本模式，根据encode自动编码解码
# f=open('py3.txt','wt',encoding='utf-8')
# f.write('你好，我爱廷廷')
# f.close()

f =open('py3.txt','rt',encoding='utf-8')
s=f.read()
print(s)