# coding=utf-8
from time import time, sleep
from SRC.common.decorator import codeException_dec
from SRC.unittest.case import TestCase
from script.common import utils
# select模块处理下拉框
from selenium.webdriver.support.ui import Select
# Keys模拟键盘操作
from selenium.webdriver.common.keys import Keys
# ActionChains模块模拟鼠标操作
from selenium.webdriver import ActionChains
# 导入堆栈类
import traceback
# 导入By类
from selenium.webdriver.common.by import By
# 导入显示等待类
from selenium.webdriver.support.ui import WebDriverWait
# 导入期望场景类
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
#等待：
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#操作下拉框：
from selenium.webdriver.support.select import Select
#操作键盘：
from selenium.webdriver.common.keys import Keys
#系统时间：
from datetime import datetime
#操作Excel：
from openpyxl import load_workbook
#sleep：
from time import *


class EasyCase(TestCase):
    def __init__(self, webDriver, paramsList):
        # 请不要修改该方法124421
        super(EasyCase, self).__init__(webDriver, paramsList)

    @codeException_dec('3')
    def runTest(self):
        driver = self.getDriver()
        param = self.param
        tool = utils

        #请在下方开始编写脚本：
        driver.find_element_by_class_name()