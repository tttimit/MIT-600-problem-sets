# 多进程
# Unix/Linux操作系统提供了一个 fork() 系统调用，它非常特殊。普通的函数调用，调用一次
# 返回一次，但是 fork() 调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复
# 制了一份（称为子进程），然后分别在父进程和子进程内返回。

# 子进程永远返回 0 ，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多
# 子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用 getppid() 就可以拿到父
# 进程的ID。

import os

print("Proccess (%s) start..." % os.getpid())

pid = os.fork()
if pid == 0:
    print("I am child process (%s) and my parent is %s.\n" % (os.getpid(), os.getppid()))
else:
    print("I (%s) just created a child process (%s).\n" % (os.getpid(), pid))
