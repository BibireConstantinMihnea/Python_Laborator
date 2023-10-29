def loop(mapping):
    list = []
    val = mapping['start']
    while val not in list:
        list.append(val)
        val = mapping[f'{val}']
    return list
print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))