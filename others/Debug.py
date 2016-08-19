# -*- coding: utf-8 -*-
# 程序的调试
# 常见的方法是使用 print() 来查看程序运行过程中某些变量的值，缺点是可能导致很多打印代码
# 另一种方法是使用 assert 断言，assert比较多的话，和print一个问题，但是可以通过在运行
# 时，添加 -O（大写的O） 来关闭assert，相当于所有的assert语句都变成 pass
# pythong3 -O err.py

def foo(s):
    n = int(s)
    assert n != 0, "n is zero!"
    return 10 / n

def main():
    foo('0')

##main()

# 第三种方法是使用 logging ，不会抛出错误，并且可以输入到文件里
# log有4个级别，分别是：debug, info, warning, error，当打开了高级别，低等级的不会
# 打印出来，最后也不用删除

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# 第四种方法
