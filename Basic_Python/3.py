nested_tuple = ((1, 2), (3, 4), (1, 2), (5, 6))
unique_elements = set(item for tpl in nested_tuple for item in tpl)
print(list(unique_elements))
