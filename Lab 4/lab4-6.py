def unique_elements(list):
    new = set(list)
    a = len(new)
    b = len(list) - a
    return (a, b)

list = [1, 2, 3, 2, 4, 3]
print(unique_elements(list))