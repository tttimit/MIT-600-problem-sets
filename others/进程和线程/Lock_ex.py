# Lock
# 多进程和多线程最大的不同，多进程中，同一个变量，各自有一份拷贝，互不影响
# 多线程中，所有的变量都由所有线程共享，因此非常危险

import threading

balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000):
        change_it(n)


# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 在存取的过程中，会出现线程安全问题，因此需要加上一把锁


balance = 0
lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.releace()


# 多个线程在执行 lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程
# 就继续等待，直到获取锁为止。  一定要注意释放锁！！


# 多核CPU

import threading
import multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
