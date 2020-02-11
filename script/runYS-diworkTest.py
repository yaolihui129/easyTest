# ！ /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/11 13:00
# @Author   : yaolh(yaolh@yonyou.com)
# @File     : runYS-dailyTest.py
# @Version  : 0.1
# DESC      : 对应Upcat的任务计划
# @Software : PyCharm
import sys
import os
from script import addPathToPython, initSettings, selectModel
# 你把原先框架的顺序修改了，修改的不对，下边这句就是把目录放到sys.path中，先执行这句才能获取到script和SRC，否则就会报错，sys无法找到script
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

addPathToPython()
initSettings()
selectModel()

from SRC.main import Main

Main('YS-diwork/租户初始化/基础数据前置.xml').run()

