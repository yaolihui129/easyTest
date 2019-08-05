#
# WebDriver原理：
# Server-Client设计模式
#
# Server：任意的浏览器
# Client：测试代码
#
# WebDriver的工作流程：
# 1.WebDriver启动目标浏览器，并绑定到指定端口。启动的浏览器实例将作为WebDriver的Remote Server。
# 2.Client端通过CommandExcuter发送HTTPRequest给Remote Server的侦听端口（通信协议：the webdriver wire protocol）
# 3.Remote Server 需要依赖原生的浏览器组件（如IEDriverServer.exe,chromedriver.exe）来转化浏览器的native调用
#
# 简单来说：
# 测试代码->CommandExcuter->浏览器
#
# 自动化技术需要得到整个团队的配合与支持
#
# 几个专有名词的区别
# 库（Library）供程序员调用
# 框架（Framework） 用户只需要使用框架提供的类和函数，即可实现全部功能
# 工具（Tool）屏蔽底层代码
#
# 自动化测试模型：
# 线性测试
# 模块化驱动测试
# 数据驱动测试
# 关键字驱动测试
#
# 关键字驱动测试：
# 做什么？
# 对谁做？
# 如何做？
#
# unittest
# 提供用例组织与执行
# 提供丰富的比较方法
# 提供丰富的日志
#
#
