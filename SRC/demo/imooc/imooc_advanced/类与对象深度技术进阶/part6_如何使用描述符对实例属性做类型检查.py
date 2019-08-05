# 如何使用描述符对实例属性做类型检查

# 使用描述符来实现需要类型检查的属性：
# 分别实现__get__,__set__,__delete__方法
# 在__set__内使用isintance函数做类型检查


class Attr(object):
	def __init__(self, name, type_):
		self.name = name
		self.type_ = type_

	def __get__(self, instance, owner):
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		if not isinstance(value, self.type_):
			raise TypeError('expected an %s' % self.type_)
		instance.__dict__[self.name] = value

	def __delete__(self, instance):
		del instance.__dict__[self.name]

class Person(object):
	name = Attr('name', str)
	age = Attr('age', int)
	height = Attr('height', float)

p=Person()
p.name ='Bob'
print(p.name)
p.age='17'