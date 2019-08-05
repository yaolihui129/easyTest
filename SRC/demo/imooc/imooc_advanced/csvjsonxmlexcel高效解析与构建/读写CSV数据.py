# 使用标准库中的csv模块，可以使用其中reader和writer完成csv的读写
from urllib.request import urlretrieve

# url='http://table.finance.yahoo.com/table.csv?s=000001.sz'
# urlretrieve(url,'pingan.csv')

import csv

# rf=open('pingan.csv','r')
# reader=csv.reader(rf)
# # for row in reader:print(row)
#
# wf=open('pinggan_copy','w')
# writer=csv.writer(wf)
#
# writer.writerow(reader.__next__())


with open('pingan.csv','r') as rf:
	reader=csv.reader(rf)
	with open('pingan2.csv','w') as wf:
		writer=csv.writer(wf)
		headers=reader.__next__()
		writer.writerow(headers) #写入头部
		for row in reader:
			if row[0]<'2016-01-01':
				break
			if int(row[5])>=50000000:
				writer.writerow(row)
print('end.')