
## f = open('ff.txt', 'r')

##try:
##    f = open('ee.txt', 'r')
##    print(f.read())
##except:
##    if f:
##        f.close()

# 使用with，精简代码
##with open('ee.txt', 'r') as f:
##    print(f.read())

with open('chinese.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        print(i.strip())

