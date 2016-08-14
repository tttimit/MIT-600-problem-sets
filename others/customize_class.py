# __str__ 当调用print()时调用    print(Student("tttimit"))
# __repr__当直接打印类的时候调用 Stduent("tttit")
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Student object (name=%s)" % self.name
    __repr__ = __str__


# __iter__  可迭代，需要返回一个iterator对象
# __next__ 方法会对iterator对象不断调用，获取下一个值
# __getItem__ 获取指定位置的值 类似 []
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):# in python2.7 should use next; 3.5 should __next__
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            if stop is None:
                raise Exception("slice must have a stop value!")
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

# __getattr__ 注意，如果重写了这个方法，需要注意保持抛出错误，否则不存在的属性返回None
class Test(object):
    def __init__(self):
        self.name = "tttimit"

    def __getattr__(self, attr):
        if attr == "score":
            return 99
##        else:
##            return lambda: 25 #返回函数也是可以的
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

#链式调用， REST API? 掉渣天
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        if path == 'users':
            return lambda user: Chain('users/%s/%s' % (self._path, user)) # lambda is awesome!
        else:
            return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__


# __call__ 直接调用实例的方法 类似 s = Student()  调用s()就是调用了__call__
# 使用 callable() 来确认一个实例或者类是否能直接调用 
class Test2(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print("My name is %s." % self.name)
