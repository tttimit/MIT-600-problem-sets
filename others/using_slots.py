####class Student(object):
####    pass
####
####s = Student()
####s.name = "Jack"
####print "s.name-->", s.name
####
######给实例绑定一个方法
####def set_age(self, age):
####    self.age = age
####
####from types import MethodType
####
####s.set_age = MethodType(set_age, s)
####s.set_age(25)
####print "s.age-->", s.age
####
######其他的实例则没有这个方法
####s2 = Student()
######s2.set_age(22)
####
####
######给类动态绑定一个方法
####def set_score(self, score):
####    self.score = score
####
####Student.set_score = set_score
####
####s.set_score(90)
####print "s.score-->", s.score
####
####s2.set_score(87)
####print "s2.score->", s2.score


##使用__slots__
class Student(object):
    __slots__ = ('name', 'age')

##对子类没用，只对当前类有用，如果子类定义了slots，则slots是自己的加上父类的slots
class GraduateStudent(Student):
    __slots__ = ('score')
