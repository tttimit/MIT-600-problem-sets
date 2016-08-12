##def log(func):
##    def wrapper(*args, **kw):
##        print('call %s():' % func.__name__)
##        return func(*args, **kw)
##    return wrapper
##
##@log
##def now():
##    print("2016-08-11")
#now() # now = log(now)
##def log(text):
##    def decorator(func):
##        def wrapper(*args, **kw):
##            print('%s %s():' % (text, func.__name__))
##            return func(*args, **kw)
##        return wrapper
##    return decorator
##
##@log('execute')
##def now():
##    print("2016-08-11")
##
##now() #相当于 now = log('execute')(now)
#execute now():
#2016-08-11
##import functools
##
####def log(func):
####    @functools.wraps(func)
####    def wrapper(*args, **kw):
####        print('call %s():' % func.__name__)
####        return func(*args, **kw)
####    return wrapper
##
##def log1(text):
##    def decorator(func):
##        @functools.wraps(func)
##        def wrapper(*args, **kw):
##            print('%s %s():' % (text, func.__name__))
##            return func(*args, **kw)
##        return wrapper
##    return decorator

import functools
def log(text=None):
    if text == None:
        @functools.wraps(func)
        def wrapper(func):
            print("no argument")
            return func(*args, **kw)
        return wrapper
    else:
        @functools.wraps(func)
        def decorator(func):
            def wrapper(*args, **kw):
                print('%s %s():' %(text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

@log
def now():
    print("2016-08-11")

##@log('nice!')
##def gg():
##    print("gali gg")

