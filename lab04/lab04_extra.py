from lab04 import *

# Q12
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    if lst == []:
        return []

    if type(lst) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst]
    
# Q13
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    
    def minx(l1,l2):
        if l1 == [] :
            return l2[0],l2[1:],[]
        elif l2 == [] :
            return l1[0],l1[1:],[]
        else:
            if l1[0]<l2[0]:
                return l1[0],l1[1:],l2
            else:
                return l2[0],l1,l2[1:]
    
    temp = []
    while lst1 != [] or lst2 != []:
        crnt,lst1,lst2 = minx(lst1,lst2)
        temp.append(crnt)
    return temp
    
            

