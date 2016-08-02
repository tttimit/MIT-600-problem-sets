#杨辉三角
#把每行看作一个list，尝试写出一个generator不断生成下一行的list

#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1

def triangles():
    l_0 = [1]
    l_1 = [1, 1]
    while True:
        yield l_0
        new_list = []
        for i in range(len(l_1) + 1):
##            print("i=" + str(i))
            if i == 0 or i == len(l_1):
                new_list.append(1)
            else:
                new_list.append(l_1[i] + l_1[i - 1])
        l_0, l_1 = l_1, new_list
    
    

