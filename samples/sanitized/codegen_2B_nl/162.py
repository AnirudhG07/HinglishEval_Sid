def string_to_md5(text):
    """
    Ek string 'text' di gayi hai, uska md5 hash equivalent string return karo.
    Agar 'text' ek khali string hai, to None return karo.
    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if isinstance(text, str):
        return md5(text).hexdigest()
    if isinstance(text, unicode):
        return md5(text.encode("ascii")).hexdigest()
    return None