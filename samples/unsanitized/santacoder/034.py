

def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    tmp = []
    for el in l:
        if el not in tmp:
            tmp.append(el)
    return tmp
