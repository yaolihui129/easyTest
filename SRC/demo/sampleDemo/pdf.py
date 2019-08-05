# coding=utf-8
import pdfkit

# url='http://www.cnblogs.com/taceywong/p/5643978.html'
# url='http://www.imooc.com/'
url='http://10.10.12.163:8088/desktop'
out='c:\\test2.pdf'
pdfkit.from_url(url, out)
pdfkit.configuration()


