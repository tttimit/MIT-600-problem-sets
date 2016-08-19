# 错误处理
# 可以使用logging模块，将错误信息保存，程序继续执行
# 通过配置，logging还可以把错误日志记录到日志文件中

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e) # 这种形式的话，会将错误栈打印出来，并且继续执行
##        print("get a error:", e) # 这种形式不会打印错误栈，只会打印e的具体类型

##main()
##print('end')

# 抛出错误，错误也是一个类，并不是凭空产生的，而是有意创建并抛出的
# 首先根据需要定义一个错误的class，选择好继承关系，然后用 raise 语句抛出一个错误实例

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value: %s" % s)
    return 10 / n

##foo('0')

# 只有在必要的时候才定义我们自己的错误类型，如果可以选择现有的错误类型，那么尽量使用内置的

# 另一种处理异常的方法，即： 捕捉到异常后，打印一下（或者记录到log中），再继续上抛
# 自己可能没法处理，所以把问题抛给更高层的代码处理，这是很常见的处理方法
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError("invalid value: %s" % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

