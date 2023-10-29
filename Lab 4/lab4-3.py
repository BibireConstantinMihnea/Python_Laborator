def compare_dicts(dict1, dict2):
    if len(dict1) != len(dict2):
        return False

    for key, value in dict1.items():
        if key not in dict2:
            return False

        value2 = dict2[key]

        if isinstance(value, dict) and isinstance(value2, dict):
            if not compare_dicts(value, value2):
                return False
        elif isinstance(value, (list, tuple, set)) and isinstance(value2, (list, tuple, set)):
            if set(value) != set(value2):
                return False
        elif value != value2:
            return False

    return True

dict_1 = {
    'a': 1,
    'b': [2, 3],
    'c': {'d', 'c'},
    'e': {'x': 4, 'y': 5}
}

dict_2 = {
    'a': 1,
    'b': [2, 3],
    'c': {'d', 'c'},
    'e': {'x': 4, 'y': 5}
}

print(compare_dicts(dict_1, dict_2))