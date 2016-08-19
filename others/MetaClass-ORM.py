# MetaClass
# MetaClass用于ORM(Object Relational Mapping 对象-关系映射，用对象来代表数据库的一行，
# 一个类代表一个表，便于代码编写)的例子，因为所有的类必须要动态定义，因为只有使用者才能够
# 根据表的定义写出对应的类来，因此需要动态定义。

# 先把调用接口写出来，比如，使用者要使用这个ORM框架，想定义一个User类来操作一个对应的数
# 据库表User，那么以下就是我们期待他写出的代码：
##class User(Model):
##    # 定义类的属性到列的映射：
##    id = IntegerField('id')
##    name = StringField('username')
##    email = StringField('email')
##    password = StringField('password')

#创建一个实例
##u = User(id = 12345, name='tttimit', email='test@test.net', password='123456')
#保存到数据库
##u.save()


#上面是使用的例子，父类Model，Field都由ORM框架提供，现在开始按照接口实现ORM框架

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 下面编写最复杂的 ModelMetaclass

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        '''
        cls:当前准备创建的类的对象
        name:类的名字
        bases:类继承的父类集合
        attrs:类的方法集合
        '''
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name #　假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# 以及基类 Model

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Micheal', email="test@11.cc", password='pppp')
u.save()
## out:
##Found model: User
##Found mapping: email ==> <StringField:email>
##Found mapping: name ==> <StringField:username>
##Found mapping: id ==> <IntegerField:id>
##Found mapping: password ==> <StringField:password>
##SQL: insert into User (email,id,password,username) values (?,?,?,?)
##ARGS: ['test@11.cc', 12345, 'pppp', 'Micheal']
                    
