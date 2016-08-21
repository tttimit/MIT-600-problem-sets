# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数

# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，
# 而是Iterator，只有用for循环迭代的时候才真正计算。

import itertools


# count()
# “无限”迭代器
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# 1
# 2
# 3
# 4
# 5
# 6
# ...infinate


# cycle()
# cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)
# 'A'
# 'B'
# 'C'
# 'A'
# 'B'
# 'C'
# 'A'
# 'B'
# 'C'
# ...

# repeat()
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)
# 'A'
# 'A'
# 'A'


# takewhile()
# 通过takewhile()等函数根据条件判断来截取出一个有限的序列
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# list(ns)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# chain()
# 把一组迭代对象串联起来，形成一个更大的迭代器
# for c in itertools.chain('ABC', 'ZLY'):
#     print(c)
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起
# for key, group in itertools.groupby('AAACCCDDDBBB'):
#     print(key, list(group))
# A ['A', 'A', 'A']
# C ['C', 'C', 'C']
# D ['D', 'D', 'D']
# B ['B', 'B', 'B']

# 实际上挑选规则是通过函数完成的, 只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的
# for key, group in itertools.groupby('AaaBbcCCddD', lambda x: x.lower()):
#     print(key, list(group))
# a['A', 'a', 'a']
# b['B', 'b']
# c['c', 'C', 'C']
# d['d', 'd', 'D']
