# -*- coding: utf-8 -*-
# 反序列化json
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("Bob", 24, 88)


##print(json.dumps(s))

# 默认情况下，dumps()方法不知道如何将一个Student对象转化为json
# dumps()方法还有一大堆可选的参数，就是用来定制序列化JSON的
# 我们需要自己实现一个用来转化的函数

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# 这样的话，就可以顺利地进行转化了
##print(json.dumps(s, default=student2dict))

# 如果下次遇到一个新的Teacher类，那么仍旧无法序列化为JSON
# 可以偷个懒，把任意class的实例变为dict：
##print(json.dumps(s, default=lambda obj: obj.__dict__))

# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class

# 同样的道理，如果要把json反序列化为一个Student对象实例，loads()方法首先转换成一个dict
# 对象，然后我们传入的object_hook函数负责把dict转化为Student实例

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
# < __main__.Student
# object
# at
# 0x7f64bff6ebe0 >

# 打印出来的是反序列化后的 Student对象
