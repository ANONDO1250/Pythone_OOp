nested_tuples = ((1, 2), (3, 4), (5, 6))
result = tuple(sum(tpl) for tpl in nested_tuples)
print(result)
