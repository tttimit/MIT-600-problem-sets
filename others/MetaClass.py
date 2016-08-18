class Hello(object):
    def hello(self, name='world'):
        print("Hello, %s." % name)

def fn(self, name='world'):
    print("hello, %s." % name)


#type()函数可以用来在代码运行时动态地构造一个类

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
print("type(Hello)=", type(Hello))
print("type(h)=", type(h))

## Metaclass
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L.add(2)
L.append(3)
print(L)

#但是普通的list并没有 add()方法
L2 = list()
##L2.add(1)
