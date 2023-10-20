tuple_list = [(1, 2), (3, 4), (5, 6)]
sum_tuple = tuple(sum(tpl) for tpl in tuple_list)
print(sum_tuple)
