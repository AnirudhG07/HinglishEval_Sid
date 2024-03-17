
def check_dict_case(dict):
    """
    Ek dictionary di gayi hai, return karo True agar saare keys lower case strings hai ya saare keys upper case strings hai, nahi to return karo False.
    Agar di gayi dictionary khali hai to function False return karega.
    Udaharan:
    check_dict_case({"a":"apple", "b":"banana"}) ka return hona chahiye True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) ka return hona chahiye False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) ka return hona chahiye False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) ka return hona chahiye False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) ka return hona chahiye True.
    """
    if len(dict) == 0:
        return False
    elif all(isinstance(key, str) for key in dict.keys()) and all(key.islower() for key in dict.keys()):
        return True
    elif all(isinstance(key, str) for key in dict.keys()) and all(key.isupper() for key in dict.keys()):
        return True
    else:
        return False

