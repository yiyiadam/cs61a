def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    return [ n - i for i in range(n+1)]
    


def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    """
    assert len(s) >= k
    "*** YOUR CODE HERE ***"
    i = 0
    while True:
        if i < k:
            yield s[i]
            i +=1
        else:
            raise ValueError("Out of range")

def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    itr_first = iter(t)
    count = 1
    
    first = next(itr_first)
    while True:
        try:
            temp = next(itr_first)
            if temp == first:
                count +=1
                if count >=k:
                    return temp
            else:
                first = temp
                count =1
        except ValueError:
            return None

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        yield n
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1  
        
        if n==1:
            yield n
        else:
            pass 