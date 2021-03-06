from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y*10 + x%10
    while x > 0:
        x, y = x//10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        if i == 1:
            print(1)
        else:
            counter(i-1)
            print(i)
    return counter(n)
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    def sel_mul(m,n):
        if m == 0:
            return 0
        if m == 1:
            return n
        else:
            return n+sel_mul(m-1,n)
    
    return sel_mul(a,b)+c

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def divid(a):
        if a == 1:
            return True
        if n%a == 0:
            return False
        else:
            return divid(a-1)
    return divid(n-1)
    
        

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    
    """ def sum_odd(m):
        idx = 1
        sums = 0
        while idx <= m:
            sums += odd_term(idx)
            idx +=2
        return sums
    def sum_even(m):
        idx = 0
        sums = 0
        while idx <= m:
            sums += even_term(idx)
            idx +=2
        return sums
    return sum_even(n) + sum_odd(n)
    """
    def switch_term(c_term):
        if c_term == odd_term:
            return even_term
        else:
            return odd_term

    def current_term(m):
        if m == 1:
            return odd_term
        else:
            return switch_term(current_term(m-1))

    def sum_all(m):
        if m == 1:
            return current_term(1)(1)
        else:
            return current_term(m)(m) + sum_all(m-1) 

    return sum_all(n)
            
        

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def counter(n, k):
        if n == 0:
            return 0
        elif n % 10 + k == 10:
            return 1 + counter(n//10, k)
        else:
            return counter(n//10, k)
    def repeating(n):
        if n == 0:
            return 0
        else:
            return counter(n // 10, n % 10) + repeating (n // 10)
    return repeating(n)