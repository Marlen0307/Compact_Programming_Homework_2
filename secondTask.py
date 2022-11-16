def get_last_element(n): return n[-1]


def sort_list_last(tuples):
    return sorted(tuples, key=get_last_element)


print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))