def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    count = 0
    for i in l:
        if i < t:
            count = count + 1
    if count == len(l):
        return True
    else:
        return False