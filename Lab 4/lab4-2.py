def char_dict(string):
    dictionary = {}
    for ch in string:
        if dictionary.get(ch) == None:
            dictionary.setdefault(ch, 1)
        else: dictionary.update({ch : dictionary.get(ch) + 1})
    return dictionary
string = "Ana are mere"
print(char_dict(string))