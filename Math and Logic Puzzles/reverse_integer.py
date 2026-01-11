'''
REVERSE INTEGER
Given an integer, return the reversed form of that integer.
No casting is allowed.
If the initial number is negative, maintain the negative in the final answer (e.g. -123 becomes -321).
'''

def reverse_integer(n):
    if n == 0:
        return 0
    
    is_neg = False
    if n < 0:
        is_neg = True
        n *= -1

    reversed = 0

    while (n != 0):
        reversed *= 10
        reversed += (n % 10)
        n //= 10

    if is_neg:
        return -reversed

    return reversed
