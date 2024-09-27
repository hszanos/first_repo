list1 = [1, [2, 3, [4, [5, 6], 7]], 8, 9, [[10]]]

def flat_list(lst, re_list = []):
    for item in lst:
        if isinstance(item, (int, float, str)):
            re_list.append(item)
        else:
            flat_list(item)
    return(re_list)

print(flat_list((list1)))