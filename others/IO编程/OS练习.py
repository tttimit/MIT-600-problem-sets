# -*- coding: utf-8 -*-
'''
1 利用os模块编写一个能实现 dir -l 输出的程序
2 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
  并打印出相对路径
'''

## 利用os模块编写一个能实现 dir -l 输出的程序
## dir -l 我猜想是类似 ls -l在Linux中的显示，类似：
## drwxr-xr-x 2 zhanglingyun zhanglingyun 4096  5月 12 12:36 FTP
## drwxrwxr-x 9 zhanglingyun zhanglingyun 4096  6月 27 16:29 mydir
import os
from datetime import datetime

def dir_l():
    files = [x for x in os.listdir('.')]
    for f in files:
        statinfo = os.stat(f)
##        print(statinfo.st_mtime)
        time = datetime.utcfromtimestamp(statinfo.st_ctime)
        if os.path.isfile(f):
            print("%-6s%-8s%s  %s" % ("file",statinfo.st_size, time, f))
        else:
            print("%-6s%-8s%s  %s" % ("dir",statinfo.st_size, time, f))


## 编写一个程序，能在当前目录以及所有子目录查找文件名包含指定字符串的文件并打印出
## 相对路径

def find_file(file_name, cur_dir='.'):
    files = [x for x in os.listdir(cur_dir)]
    for f in files:
        if cur_dir != '.':
            f = os.path.join(cur_dir, f)
        if os.path.isfile(f):       
            if file_name in os.path.split(f)[1]:
                    print(f)
        elif os.path.isdir(f):
            find_file(file_name, f)


if __name__ == '__main__':
#    dir_l()
    find_file('et')
