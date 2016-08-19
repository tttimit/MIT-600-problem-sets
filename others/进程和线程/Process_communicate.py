# 进程间通信
# Python的 multiprocessing 模块包装了底层的机制，提供了 Queue、Pipes等方式来交换数据

# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从中读数据

import os
import random
import time
from multiprocessing import Process, Queue


# 写数据进程执行的代码：
def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A', 'B', 'C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码：
def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    print("ready to go...")
    pw.start()

    pr.start()

    pw.join()

    pr.terminate()
