tuple_list = [(1, 2), (3, 4), (5, 6)]
updated_list = [tuple(x + 1 for x in tpl) for tpl in tuple_list]
print(updated_list)
