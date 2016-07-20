
##
##indent = ''
##def f(s):
##    global indent
##    indent += '  '
##    if len(s) <= 1:
####        print("return", s)
##        return s
##    g = f(f(s[1:])) + s[0]
##    print(indent + "f(\'" + s + "\')=" + g)
##    indent = indent[:-2]
##    return g
##
##print(f('mat'))
##print(f('math'))
##
##def findAll(wordList, lStr):
##    """assumes: wordList is a list of words in lowercase.
##                lStr is a str of lowercase letters.
##                No letter occurs in lStr more than once
##       returns: a list of all the words in wordList that contain
##                each of the letters in lStr exactly once and no
##                letters not in lStr"""
##    result = []
##    dic = {}
##    for s in lStr:
##        dic[s] = 1
##    for word in wordList:
##        if len(word) > len(lStr):
##            continue
##        else:
##            temp_dic = dic.copy()
##            i = 0
##            for char in word:
####                print("word:", word, "char:", char, "temp_dic:", temp_dic)
##                if char not in temp_dic.keys():
##                    break
##                else:
##                    del temp_dic[char]
##                    i += 1
##                if i == len(word):
##                    result += [word,]
####                print("word:", word, "temp_dic:",temp_dic)
##    return result
##
##from ps3a import *
####FILE_NAME = "words_test.txt"
##FILE_NAME = "words.txt"
##
##wordList = load_words(FILE_NAME)
##lStr = "boadt"
##print(findAll(wordList, lStr))
##
##def addVectors(v1, v2):
##    l1 = v1.copy()
##    l2 = v2.copy()
##    if len(l1) > len(l2):
##        for k in range(len(l2)):
##            l1[k] += l2[k]
##        return l1
##    else:
##        for m in range(len(l1)):
##            l2[m] += l1[m]
##        return l2
##
##v1 = [4, 5]
##v2 = [1, 2, 3]
##print(addVectors(v1, v2))
##print(v1)
##print(v2)

##def f(s, d):
##    for k in d.keys():
##        d[k] = 0
##    for c in s:
##        if c in d:
##            d[c] += 1
##        else: d[c] = 0
##    return d
##
##def addUp(d):
##    result = 0
##    for k in d:
##        result += d[k]
##    return result
##
##d1 = {}
##d2 = d1
##d1 = f('abbc', d1)
##print(addUp(d1))
##d2 = f('bbcaa', d2)
##print(addUp(d2))
##print(f('', {}))
##print(result)

##def logBase2(n):
##    import math
##    return math.log(n, 2)
##
##def f(n):
##    if n < 1:
##        return
##    curDigit = int(logBase2(n))
##    ans = 'n = '
##    while curDigit >= 0:
##        if n%(2**curDigit) < n:
##            ans = ans + '1'
##            n = n - 2**curDigit
##        else:
##            ans = ans + '0'
##        curDigit -= 1
##    return ans
##
##for i in range(3):
##    print(f(i))
