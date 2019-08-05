import telnetlib

# 配置选项
Host = '10.10.12.140'  # Telnet服务器IP
username = 'root'  # 登录用户名
password = 'root'  # 登录密码
finish = ':~$ '  # 命令提示符（标识着上一条命令已执行完毕）

# 连接Telnet服务器
tn = telnetlib.Telnet(Host,23)
# 输入登录用户名
tn.read_until(b'login: ')
tn.write(username + '\n')
# 输入登录密码
tn.read_until('Password: ')
tn.write(password + '\n')
# 登录完毕后，执行ls命令
tn.read_until(finish)
tn.write('ls\n')
# ls命令执行完毕后，终止Telnet连接（或输入exit退出）
tn.read_until(finish)
tn.close()  # tn.write('exit\n')
