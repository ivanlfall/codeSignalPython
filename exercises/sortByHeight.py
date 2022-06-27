def sortByHeight(a):
    position_trees = [index for index in range(len(a)) if a[index] == -1]
    aux_list = sorted([item for item in a if item != -1])

    for pos in position_trees:
        aux_list.insert(pos, -1)

    return aux_list


print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))