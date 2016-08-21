## 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
##
## someone@gmail.com
## bill.gates@microsoft.com
##
## 版本二可以验证并提取出带名字的Email地址：
##
## <Tom Paris> tom@voyager.org

# version1

import re

re_email = re.compile(r'^[\w.]*@\w+.[a-zA-Z]+$')

# print(re_email.match('someone@gmail.com'))
# print(re_email.match('bill.gates@microsoft.com'))
# print(re_email.match('b@m.c'))
#
# print(re_email.match('b'))
# print(re_email.match('b@m.'))
# print(re_email.match('b@.c'))

# version2

re_email2 = re.compile(r'^(\w+).?(\w*)@\w+.[a-zA-Z]+$')


def test(email):
    if re_email2.match(email):
        # print("got a match-->%s" % email)
        groups = re_email2.match(email).groups()
        # print("groups-->", groups)
        if groups[1] != '':
            print("<%s %s> %s" % (groups[0], groups[1], email))
        else:
            print(email)
    else:
        print("%s is not a valid email address!" % email)
        # print("===")


test("bill.gates@microsoft.com")
test("Tom.Paris@hotmail.com")
test("timit.cloud@gmail.com")
test("timit_cloud@qq.com")
test("timitcloud@live.cn")
# test("1@1.1")
# test("gogogo")
# test("@1")
# test("tt.cc")
# test("__@__.__")
# test("123.gge.213@gg.")
# test("sdf.sadf.dfs@gg.gg")
# test("sd.df.asd.sdf.sdf.sdf@gg.c")
# test(".@.")
