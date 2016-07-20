##x = 10.0
##for i in range(10):
##    x += 0.1
##print(x == 11.0)
##for i in range(10):
##    x -= 0.1
##print(x == 10.0)

##def buildCodeBook():
##    letters = '.abcdefghijklmnopqrstuvwxyz'
##    codeBook = {}
##    key = 0
##    for c in letters:
##        codeBook[key] = c
##        key += 1
##    return codeBook
##
##def decode(cypherText, codeBook):
##    plainText = ''
##    for e in cypherText:
##        if e in codeBook:
##            plainText += codeBook[e]
##        else:
##            plainText += ' '
##    return plainText
##
##codeBook = buildCodeBook()
##msg = (3, 2, 41, 1, 0)
##print(decode(msg, codeBook))

##def addVectors(v1, v2):
##    c1 = v1.copy()
##    c2 = v2.copy()
##    result = []
##    r = min(len(v1), len(v2))
##    for i in range(r):
##        result.append(v1[i] + v2[i])
##    if len(v1) > r:
##        for i in range(len(v1) - r):
##            result.append(v1[i+r])
##    else:
##        for i in range(len(v2) - r):
##            result.append(v2[i + r])
##    return result
##
##print(addVectors([4, 5], [1, 2, 3]))
##print(addVectors([], []))

##def getLines():
##    inputs = []
##    while True:
##        line = int(input('Enter a positive integer, -1 to quit: '))
##        if line == -1:
##            break
##        inputs.append(line)
##    return inputs
##total = 0
##for e in getLines():
##    total += e
##print(total)

##def f(s):
##    """Assume type(s) == str"""
##    d = {}
##    for c in s:
##        if c in d.keys():
##            d[c] += 1
##        else:
##            d[c] = 1
##    x = None
##    for k in d.keys():
##        if x == None:
##            x = d[k]
##            y = k
##        elif d[k] > x:
##            x = d[k]
##            y = k
##    return y
##print(f('abbc'))
##for i in range(100):
##    print(f('bbcaa'))
##
##
##print(f(''))
##

def f(L):
    result = []
    for e in L:
        if type(e) != list:
##            print("result:", result, " append:", e)
            result.append(e)
        else:
            return f(e)
    print("about to return:", result)
    return result

##print(f('3'))
##print(f(3))
##print(f([1, [[[2], 'a', 'c'], ['a', 'b']], (3, 4)])) #shoule return [2]

