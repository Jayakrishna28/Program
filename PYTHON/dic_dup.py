my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 5}
res_dict = {}
for key, value in my_dict.items():
    if value not in res_dict.values():
        res_dict[key] = value
print(res_dict)