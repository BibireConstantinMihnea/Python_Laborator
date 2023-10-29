def list_op(sets):
    dict = {}
    for i, set1 in enumerate(sets):
        for j, set2 in enumerate(sets):
            if i != j and j > i:
                dict[f"{set1} | {set2}"] = set1.union(set2)
                dict[f"{set1} & {set2}"] = set1.intersection(set2)
                dict[f"{set1} - {set2}"] = set1.difference(set2)
                dict[f"{set2} - {set1}"] = set2.difference(set1)

    return dict

sets = [{1,2}, {2, 3}]
print(list_op(sets))