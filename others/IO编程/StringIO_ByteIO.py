# StringIO 是在内存中读写str

from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World!')
# 使用getvalue()方法来获取值
print('StringIO f=', f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后和读取文件一样读取
f = StringIO('Hello!\nHi!\nWorld!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

print('-----------')

# BytesIO 是在内存中操作二进制数据

from io import BytesIO
f = BytesIO()

# 注意，写入的不是中文，而是以utf-8编码后的二进制值
f.write('中文'.encode('utf-8'))
print('BytesIO f=', f.getvalue())

# 要读取BytesIO，与StringIO类似

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8'))


