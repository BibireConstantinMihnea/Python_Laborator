def list_op(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    union = list(set1.union(set2))
    intersection = list(set1.intersection(set2))
    a_dif_b = list(set1.difference(set2))
    b_dif_a = list(set2.difference(set1))
    print(f"Reuniunea = {union}\nIntersectia = {intersection}\nA - B = {a_dif_b}\nB - A = {b_dif_a}")

lista1 = [1, 2, 3]
lista2 = [4, 5, 1]
list_op(lista1, lista2)