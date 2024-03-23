list1 = [1, [2, 3, [4, [5, 6], 7]], 8, 9, [[10]]]

def flatten_list(list_to_flatten):
    flat_list = []
    for row in list_to_flatten:
        flat_list.extend(row)
    return flat_list

print(flatten_list(list1))
