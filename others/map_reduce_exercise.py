##def normalize(name):
####    return name.capitalize()
##    return name[0].upper() + name[1:].lower()
##
##input = ['adam', 'LISA', 'barT']
###expcet output: ['Adam', 'Lisa', 'Bart']
##output= map(normalize, input)
##print(list(output))

##from functools import reduce
##def prod(L):
##    return reduce(lambda x, y: x * y, L)
##
##L = [2, 3, 4, 5]
##print("2 * 3 * 4 * 5 =", prod(L))
##    

from functools import reduce
##def char2int(s):
##    result_list = []
##    for i in s:
##        if i == '.':
##            result_list.append('.')
##        else:
##            result_list.append(int(i))
##    print("char2int", result_list)
##    return result_list
##
##l = char2int('0.22222')
##
##def chars2float(l):
##    result = 0.0
##    for i in l:
##        if i != '.':
##            result = result * 10 + i
##    if '.' in l:
##        index = l.index('.')
##        result = result / 10 ** (len(l) - index - 1)
##    print("chars2float:", result)
##    return result
##
##chars2float(l)

def char2int(char):
    dic = {'0':0, '1':1, '2': 2, '3': 3, '4':4, '5':5, '6':6, \
           '7':7, '8':8, '9': 9, '.': '.', '-': '-'}
    return dic[char]

##print("char2int:", char2int('1'))
##print("char2int:", char2int('.'))
##print(list(map(char2int, '234')))


def str2float(s):
    if not isinstance(s, str):
        raise TypeError("argument should be a string!")
    else:
        result = 0.0
        factor = 1
        if '-' in s:
            factor = -1
            char_list = list(map(char2int, s[1:]))
        else:
            char_list = list(map(char2int, s))
        if '.' in s:
            index = s.index('.')
            char_list = filter(lambda x: x != '.', char_list)
            result = reduce(lambda x, y: x * 10 + y, char_list)
            result = result / 10 ** (len(s) - index - 1)
        else:
            retult = reduce(lambda x, y: x * 10 + y, char_list)
    return factor * result  

print('str2float(\'123.456\')=', str2float('123.456'))
print('str2float(\'.456\')=', str2float('.456'))
print('str2float(\'123.45776\')=', str2float('123.45776'))
print('str2float(\'123.45600\')=', str2float('123.45600'))
print('str2float(\'-0.0456\')=', str2float('-0.0456'))


