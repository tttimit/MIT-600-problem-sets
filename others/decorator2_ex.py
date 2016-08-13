import functools

##def log(func):
##    @functools.wraps(func)
##    def wrapper(*args, **kw):
##        print('call %s():' % func.__name__)
##        return func(*args, **kw)
##    return wrapper
##
##@log
##def now():
##    print("2016-08-11")


##def log1(text):
##    def decorator(func):
##        @functools.wraps(func)
##        def wrapper(*args, **kw):
##            print("%s %s():" %(text, func.__name__))
##            return func(*args, **kw)
##        return wrapper
##    return decorator
##
##@log1("hello")
##def now2():
##      print("nihao")


##def log(func):
##    @functools.wraps(func)
##    def wrapper(*args, **kw):
##        print("begin call")
##        return func(*args, **kw), print("end call")
##    return wrapper
##
##
##    
##@log
##def t1():
##    print("t1 running")
##
##@log('execute')
##def t2():
##    print("t2 running")
