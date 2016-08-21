# 小结
#
# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（
# 因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在
# 不存储明文口令的情况下验证用户口令。


# keyword: md5 sha1 "add salt"

import hashlib

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5.update('how to use md5 '.encode('utf-8'))
md5.update('in python hashlib?'.encode('utf-8'))

# print(md5.hexdigest())

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))


# print(sha1.hexdigest())

# 练习

# 根据用户输入的口令，计算出存储在数据库中的MD5口令


def calc_md5(password):
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


db = {
    'michael': '3704e81a667432bebb436054e64db0e8',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    if calc_md5(password) == db[user]:
        print("logging success!")
    else:
        print("wrong password!")


# login('michael', '123456')

# 练习
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5 ==> 加盐
# 可以通过把登录名作为Salt的一部分来计算MD5, 从而实现相同口令的用户也存储不同的MD5

db = {}


def get_md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    # print('md5:', m.hexdigest())
    return m.hexdigest()


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


def login(username, password):
    if username not in db.keys():
        print("user not found!")
    elif db[username] == get_md5(password + username + 'the-Salt'):
        print("%s logging successfully!" % username)
    else:
        print("wrong password!")


register('zly', 'aaa123')
register('bob', 'aaa123')

login('zly', 'aaa12')
login('bob', 'aaa123')
login('bob1', 'aaa123')
