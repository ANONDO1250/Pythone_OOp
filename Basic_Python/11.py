tuple_list = [(1, 2), (3, 4), (5, 6)]
new_list = [tpl[:-1] + (7,) for tpl in tuple_list]
print(new_list)
my_tuple = (5, 2, 8, 1, 3)
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)
