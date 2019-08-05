import smtplib
from email.header import Header
from email.mime.text import MIMEText

jsonData={
	'smtpServer':'mail.yonyou.com',
	'user':'wangand@yonyou.com',
	'password':'',
	'sender':'wangand@yonyou.com',
	'receiver':'wangand@yonyou.com',
}

def sendMail(sender,receiver,subject,message):
	try:
		smtp=smtplib.SMTP()
		smtp.connect(jsonData['smtpServer'])
		smtp.login(jsonData['user'],jsonData['password'])
		msg=MIMEText('<html><h1>%s</h1></html>'%message,'html','utf-8')
		msg['Subject']=Header(subject,'utf-8')
		smtp.sendmail(sender,receiver,msg.as_string())
	except Exception as e:
		print(e)


if __name__=='__main__':
	sender='wangand@yonyou.com'
	receiver='wangand@yonyou.com,541175593@qq.com'
	subject='Hello Me'
	msg='Hello context'
	sendMail(sender,receiver,subject,msg)
	print('发送成功')
