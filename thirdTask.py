def sort_dictonaries(dictonaries_to_be_sorted):
    key_to_sort_by = input('Sort by:')
    if key_to_sort_by not in dictonaries_to_be_sorted[0]:
        key_to_sort_by = 'color'
    sorted_models = sorted(dictonaries_to_be_sorted, key=lambda x: x[key_to_sort_by])
    return sorted_models


test_dicts = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
              {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(sort_dictonaries(test_dicts))
