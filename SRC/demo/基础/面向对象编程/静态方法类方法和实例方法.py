def foo(x): #函数
	print('executing foo(%s)'%x)

'''
实例方法，类方法，静态方法的区别
实例方法：只能通过实例调用
类方法：可以通过实例调用，也可以通过类调用，方法内可以调用实例本身
静态方法：可以通过实例调用，也可以通过类调用，但是方法内无法调用实例，不包含参数self或cls
'''

class A(object):
	def foo(self,x):#实例方法
		print('executing foo(%s,%s)'%(self,x))

	@classmethod
	def class_foo(cls,x):#类方法
		print('executing class_foo(%s,%s)'%(cls,x))

	@staticmethod
	def static_foo(x):#静态方法
		print('executing static_foo(%s)'%x)

a=A()
a.foo('tingting')
A.class_foo('wangan')
A.static_foo('wangan and tingting')

