# -*- coding: utf-8 -*-
# 多线程环境中，每个线程有自己的数据需要处理，使用局部变量比较好
# 但是，如果有全局变量需要操作，那么可以加锁来避免线程安全问题
# 另外，局部变量使用起来也比较麻烦，那就是函数之间需要各种传递，如果函数很多，那么传递
# 起来，有种炸裂的感觉

# 如果用全部变量的话，也不行，因为每个线程处理的是不同的对象，不能共享

# 一种解决办法是，用一个dict，用线程作为key，将对应的对象作为value存储
# 这种方法有点丑陋，Python提供了ThreadLocal来处理这种任务


import threading

local_school = threading.local()


def process_student():
    std = local_school.student
    print("Hello, %s (in %s)" % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=("Alice",), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=("Bob",), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# ThreadLocal最常用的地方就是为每个线程绑定一个数据库链接，HTTP请求，用户身份信息等，这样
# 一个线程的所有调用到的处理函数都可以非常方便地访问这些资源

# 一个ThreadLocal变量虽然是全局变量，但是每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个参数之间互相传递的问题
