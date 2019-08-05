# 如何派生内置不可变类型并修改实例化行为
# 我们想自定义一种新类型的元祖，对于传入的可迭代对象，
# 我们只保留作其中int类型且值大于0的元素，例如：
# intTuple([1,-1,'abc',6,['x','y'],3])=>(1,6,3)

# 要求intTuple 是内置tuple的子类，如何实现？


class IntTuple(tuple):
	def __new__(cls, iterable):
		g=(x for x in iterable if isinstance(x,int) and x>0)
		return super(IntTuple, cls).__new__(cls,g)



t =IntTuple([1,-1,'abc',6,['x','y'],3])
print(t)


# 定义类IntTuple 继承内置tuple ，并实现__new__，修改实例化行为
