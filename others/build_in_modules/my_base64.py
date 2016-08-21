# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
#
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
#
# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，
# 所以，很多Base64编码后会把=去掉：

# 标准Base64:
# 'abcd' -> 'YWJjZA=='
# 自动去掉=:
# 'abcd' -> 'YWJjZA'

# 练习
# 请写一个能处理去掉=的base64解码函数

import base64


def safe_base64_decode(s):
    '''

    Args:
        s: bytes of string

    Returns: append b'=' to the end of s, until len(s) % 4 == 0

    '''
    while len(s) % 4 != 0:
        s = s + b'='
    return base64.b64decode(s)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
