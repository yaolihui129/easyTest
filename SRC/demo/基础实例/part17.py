# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：利用while语句,条件为输入的字符不为'\n'。

s=input('please input a line:')
dct=dict.fromkeys(s,0)
print(dct)

for x in s:
	dct[x]+=1
print(dct)
