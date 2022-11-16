def convert_strings_to_list(str_list):
    map_result = map(list, str_list)
    return list(map_result)


print(convert_strings_to_list(['test', 'string 2', 'string 3', 'string 4', 'test']))
