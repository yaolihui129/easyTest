#如何判断字符串a是否以字符串b开头或结尾
# 实际案例：某文件系统目录下有一系列文件：
# quicksort.c
# graph.py
# heap.java
# install.sh
# stack.cpp
# 编写程序给其中所有.sh文件和.py文件加上用户可执行权限

import os,stat

res=os.listdir('demoFiles')
res=[name for name in res if name.endswith(('.sh','.py'))]
print(res)

#修改权限
res=os.stat('demoFiles/graph.py').st_mode
print(oct(res)) #转换成8进制

# os.chmod('demoFiles/graph.py',os.stat('demoFiles/graph.py').st_mode|stat.S_IXUSR)
os.chmod('demoFiles/graph.py',stat.S_IWUSR)
res=os.stat('demoFiles/graph.py').st_mode
print(oct(res)) #转换成8进制

# Python修改文件权限
# os.chmod()方法 此方法通过数值模式更新路径或文件权限。该模式可采取下列值或按位或运算组合之一：
# stat.S_IXOTH: 其他用户有执行权0o001
# stat.S_IWOTH: 其他用户有写权限0o002
# stat.S_IROTH: 其他用户有读权限0o004
# stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
# stat.S_IXGRP: 组用户有执行权限0o010
# stat.S_IWGRP: 组用户有写权限0o020
# stat.S_IRGRP: 组用户有读权限0o040
# stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
# stat.S_IXUSR: 拥有者具有执行权限0o100
# stat.S_IWUSR: 拥有者具有写权限0o200
# stat.S_IRUSR: 拥有者具有读权限0o400
# stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
# stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
# stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
# stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
# stat.S_IREAD: windows下设为只读
# stat.S_IWRITE: windows下取消只读
# 语法：
# os.chmod(path, mode);