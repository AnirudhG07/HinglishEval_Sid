

def correct_bracketing(brackets: str):
    """
    brackets ek string hai "(" aur ")" ka.
    return True agar har opening bracket ka ek corresponding closing bracket ho.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    if brackets == brackets[1:]:
        return False
    else:
        return brackets[0] == '('

