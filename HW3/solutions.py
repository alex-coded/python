from input_verification_functions import *
from collections import Counter


def get_reunited_sets(set1, set2):
    return set1.union(set2)


def get_intersected_sets(set1, set2):
    return set1.intersection(set2)


def get_set_from_reunited_lists(list1, list2):
    return set(list1).union(set(list2))


def get_set_from_intersected_lists(list1, list2):
    return set(list1).intersection(set(list2))


def exercise1(a, b):
    """
    Calculates the intersection, reunion,
    and difference between the 2 lists passed as arguments
    :param a: the first list
    :param b: the second list
    :return: a list of sets containing a intersected with b,
    a reunited with b, a - b, b - a
    """
    if (not check_integer_list(a)) \
            or not check_integer_list(b):
        return "Invalid lists"

    list_of_sets = list()
    list_of_sets.append(get_set_from_intersected_lists(a, b))
    list_of_sets.append(get_set_from_reunited_lists(a, b))
    list_of_sets.append(set(a) - set(b))
    list_of_sets.append(set(b) - set(a))
    return list_of_sets


def exercise2(string):
    """
    Calculates the frequency of characters in a string
    *Count* collection counts elements from an input iterable
    :param string: a string
    :return: a dictionary with the character frequency
    """
    if not is_string(string):
        return "Invalid input"
    res = dict(Counter(string))
    return res


def check_equal_dict(depth1, depth2, depth) -> (bool, list):
    """
    Checks recursively if dictionaries are equal
    """

    if type(depth1) == type(depth2):
        if type(depth1) is dict:
            equal = True
            diff = []
            for lab1, lab2 in zip(sorted(depth1.keys()), sorted(depth2.keys())):  # for  labels
                if lab1 != lab2:
                    equal = False
                    diff.append((lab1, lab2, "depth = " + str(depth), "the keys are not equal"))
                    continue
                check_equal = check_equal_dict(depth1[lab1], depth2[lab1], depth + 1)
                if not check_equal[0]:
                    equal = False
                    diff += check_equal[1]
            else:
                return equal, diff
        if depth1 != depth2:
            return False, [(depth1, depth2, "depth = " + str(depth), "are not equal")]
        else:
            return True, []
    else:
        return False, [(depth1, depth2, "depth = " + str(depth), "encountered different type")]


def exercise3(d_1: dict, d_2: dict) -> list:
    """
    Compares two dictionaries recursively
    """
    return check_equal_dict(d_1, d_2, 0)[1]


def build_xml_element(tag: str, content: str, **components) -> str:
    """'
    Exercise4
    Build and return a string that represents the corresponding XML element
    """

    return "<{} {} >{}</{}>".format(
        tag,
        ', '.join(["{}={}".format(key, value) for key, value in components.items()]),
        content,
        tag
    )


def check_input_dict_validator(validation_rules, dictionary):
    if not is_set(validation_rules) or not is_dict(dictionary):
        return False

    for rule in validation_rules:
        if len(rule) != 4:
            return False
    return True


def validate_dict(validation_rules, dictionary):
    """
    Checks if the dictionary satisfies the given rules
    :param validation_rules: a set of tuples with 4 values each (key, prefix, middle, suffix)
    :param dictionary: the dictionary
    :return: True if matches all the rules, False otherwise
    """

    if not check_input_dict_validator(validation_rules, dictionary):
        return "Invalid input"

    for rule in validation_rules:
        value = dictionary.get(rule[0])

        if value is None:
            return False

        if not value.startswith(rule[1]) or not value.__contains__(
                rule[2]) or not value.endswith(rule[3]):
            return False
    return True


def exercise5(validation_rules, dictionary):
    return validate_dict(validation_rules, dictionary)


def exercise6(list_of_elm):
    """
    Calculates unique and duplicates in a list
    intersection_update() - removes the unwanted items from the original set
    intersection() - returns a new set, with the duplicates
    :param list_of_elm: a list
    :return: a tuple (a,b), where a represents the nr of unique elements in the list
    and b the duplicate elm
    """

    if not check_integer_list(list_of_elm):
        return "Invalid input"

    unique_elm = set(list_of_elm)
    return len(unique_elm), len(list_of_elm) - len(unique_elm)


def exercise7(*sets):
    """
    Calculates intersection, reunion and difference for all given sets 2 by 2
    :param sets: a variable number of sets
    :return: a dictionary containing the |, &, - from all sets 2 by 2
    """

    for singular_set in sets:
        if not is_set(singular_set):
            return "Invalid input"

    result = dict()
    list_of_sets = list()
    for singular_set in sets:
        list_of_sets.append(singular_set)
    for i in range(len(list_of_sets)):
        for j in range(i + 1, len(list_of_sets)):
            if list_of_sets[i] != list_of_sets[j]:
                result[str(list_of_sets[i]) + ' | ' + str(list_of_sets[j])] = \
                    get_reunited_sets(list_of_sets[i], list_of_sets[j])
                result[str(list_of_sets[i]) + ' & ' + str(list_of_sets[j])] = \
                    get_intersected_sets(list_of_sets[i], list_of_sets[j])
                result[str(list_of_sets[i]) + ' - ' + str(list_of_sets[j])] = list_of_sets[i] - list_of_sets[j]
                result[str(list_of_sets[j]) + ' - ' + str(list_of_sets[i])] = list_of_sets[j] - list_of_sets[i]
    return result


def exercise8(mapping):
    """
    Iterate through a map where the value of the current key
    is the key for the next value until we find a loop
    :param mapping: a dictionary
    :return: a list of objects obtained
    """

    if not is_dict(mapping):
        return "Invalid input"

    visited_keys = list()
    cur_value = "start"
    while cur_value not in visited_keys:
        if cur_value in mapping:
            visited_keys.append(cur_value)
            cur_value = mapping[cur_value]
        else:
            break
    return visited_keys


def exercise9(*args, **kwargs):
    """
    Calculates the number of positional arguments
    whose values can be found among keyword arguments values
    :return: integer with nr of matching values
    """

    pos_arg = set()
    keyword_arg = set()

    for arg in args:
        pos_arg.add(int(arg))

    for arg in kwargs:
        keyword_arg.add(int(kwargs[arg]))

    return len(get_intersected_sets(pos_arg, keyword_arg))