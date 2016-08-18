# 对 fact(n) 编写doctest并执行
def fact(n):
    '''
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(1)
    1
    >>> fact(5)
    120
    >>> fact(2)
    2
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
