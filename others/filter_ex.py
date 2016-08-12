def is_palindrome(n):
    str_of_n = str(n)
    return str_of_n == str_of_n[::-1]
        

output = filter(is_palindrome, range(1, 1000))
print(list(output))
