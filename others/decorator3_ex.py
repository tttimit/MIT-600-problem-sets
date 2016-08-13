Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py 
>>> now()
call now():
2016-08-11
>>> 
 RESTART: D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py 

Traceback (most recent call last):
  File "D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py", line 10, in <module>
    @log
  File "D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py", line 4, in log
    @functions.wraps(func)
NameError: global name 'functions' is not defined
>>> 
 RESTART: D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py 
>>> now.__name__
'now'
>>> now
<function now at 0x0000000003C7C3C8>
>>> now()
call now():
2016-08-11
>>> 
 RESTART: D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py 
>>> now.__name__
'wrapper'
>>> 
 RESTART: D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py 

Traceback (most recent call last):
  File "D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py", line 24, in <module>
    @log1("hello")
  File "D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py", line 16, in log1
    @functools.wraps(func)
NameError: global name 'func' is not defined
>>> 
 RESTART: D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py 

Traceback (most recent call last):
  File "D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py", line 24, in <module>
    @log1("hello")
  File "D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py", line 16, in log1
    @functools.wraps(func)
NameError: global name 'func' is not defined
>>> 
 RESTART: D:/works/Python-works/MIT-600-problem-sets/others/decorator2_ex.py 
>>> now2()
hello now2():
nihao
>>> n = log1("log1")lambda _:print("gali gg")
SyntaxError: invalid syntax
>>> n

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> n = log1("log1")(lambda _:print("gali gg"))
SyntaxError: invalid syntax
>>> n = log1("log1")(lambda x:print("gali gg"))
