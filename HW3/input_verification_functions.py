def is_digit(number):
    if not isinstance(number, int):
        return False
    return True


def is_string(str1):
    if not isinstance(str1, str):
        return False
    return True


def check_integer_list(ls):
    return [s for s in ls if is_digit(s)]


def check_string_list(ls):
    return [s for s in ls if is_string(s)]