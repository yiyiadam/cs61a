def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    def gcd(a,b):
        c=a%b
        if c == 0:
            return b;
        else:
            return gcd(b,c)
    d = gcd(a,b);
    return a*b//d

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"

    def is_digits(n):
        while n>=1:
            yield n%10
            n = n//10
    a = [i for i in is_digits(n)]
    digits = set([i for i in is_digits(n)])
    return len(digits)