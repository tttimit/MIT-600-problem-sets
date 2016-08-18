# 使用pdb调试器

##s = '0'
##n = int(s)
##print(10 / n)

# python -m pdb err.py

# 输入l来查看代码

# 输入n来单步执行

# 任何时候输入p 变量名 来查看变量

# 输入q退出

## 缺点是太麻烦，如果有1000行代码，需要操作太多次
## 另一个方法就是，使用 pdb.set_trace()，不需要单步执行，只需要在需要的地方
## 放置一个 pdb.set_tarce()，就可以设置一个断点

## 用 n 单步执行，l打印代码，p 变量名来查看变量，c继续运行，q 退出

import pdb

s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)
