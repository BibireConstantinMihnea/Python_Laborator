#1.
# def list_op(lista1, lista2):
#     set1 = set(lista1)
#     set2 = set(lista2)
#     union = list(set1.union(set2))
#     intersection = list(set1.intersection(set2))
#     a_dif_b = list(set1.difference(set2))
#     b_dif_a = list(set2.difference(set1))
#     print(f"Reuniunea = {union}\nIntersectia = {intersection}\nA - B = {a_dif_b}\nB - A = {b_dif_a}")

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 1]
# list_op(lista1, lista2)
#----------------------------------------------------
#2.
# def char_dict(string):
#     dictionary = {}
#     for ch in string:
#         if dictionary.get(ch) == None:
#             dictionary.setdefault(ch, 1)
#         else: dictionary.update({ch : dictionary.get(ch) + 1})
#     return dictionary
# string = "Ana are mere"
# print(char_dict(string))
#----------------------------------------------------
#3. ?????????????????????????????????
# def compare_dict(d1,d2):
#     for entry in d1:
#         if d2.get(entry) == None:
#             return False
#         elif d2.get(entry) != d1[entry]:
#             return False
#     return True
#----------------------------------------------------
#4.
def build_xml_element(tag, content, **kwargs):
    attributes =  "".join(f'{key}="{\\"{value}\\"}"' for key, value in kwargs.items())
    element = f"<{tag} {attributes}>{content}</{tag}>"
    return element

print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))



