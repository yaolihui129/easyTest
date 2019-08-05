# 如何调整字符串中文本的格式

# 解决方案：使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，
# 捕获每个部分内容，在替换字符串中调整各个捕获组的顺序

import re
log='2016-05-23'
res=re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log)
print(res)