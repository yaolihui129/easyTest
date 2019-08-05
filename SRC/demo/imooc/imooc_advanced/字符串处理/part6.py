# 如何去掉字符串中不需要的字符

# 1.过滤掉用户输入中前后多余的空白字符
# '   nick2008@gmail.com     '
# 2.过滤某windows下编辑文本中的'\r'
# 'hello world\r\n'
# 3.去掉文本中的unicode组合符号（音调）


# 方法一：字符串strip(),lstrip(),rstrip()方法去掉字符串两端的字符
# 方法二：删除单个固定位置的字符，可以使用切片+拼接的方式
# 方法三：字符串的replace()方法或正则表达式re.sub()删除任意位置字符
# 方法四：字符串translate()方法，可以同时删除多种不同字符

# 方法一：
s='   abc   123   '
res=s.strip()
print(res)

res=s.lstrip()
print(res)

res=s.rstrip()
print(res)

s='----123++++++'
res=s.strip('-+')
print(res)

#方法二：
s='abc:123'
res=s[:3]+s[4:]
print(res)

# 方法三
s='\tabc\t123\txyz'
print(s)
res=s.replace('\t','')
print(res)

s='\tabc\t123\txyz\ropq'
import re
res=re.sub('[\t\r]','',s)
print(res)

#方法四：
# str.translate() #将一个字符映射到另一个字符
s='abc1230323xyz'

#python3中 bytearray.maketrans()、bytes.maketrans()、str.maketrans()
tran=str.maketrans('abcxyz','xyzabc')
print(tran)

res=s.translate(tran)
print(res)
res=res.translate(tran)
print(res)
