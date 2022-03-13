def euclid(a, b):
    '''
        parameters:
            a -- int
            b -- int
        returns:
            path_length -- int
        description:
            using Euclid's algorithm
    '''
    a = a if a > 0 else -a
    b = b if b > 0 else -b
    if b > a:
        a, b = b, a
    if b == 0:
        ret = a
    else:
        ret = euclid(b, a - (a // b) * b)
    return ret
