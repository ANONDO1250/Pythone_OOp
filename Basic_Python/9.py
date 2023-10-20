tuple_list = [(1, 5), (3, 8), (9, 2), (6, 4)]
max_difference = max(abs(tpl[0] - tpl[1]) for tpl in tuple_list)
print(max_difference)
