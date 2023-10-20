tuple_list = [(1, 2), (3, 4), (1, 2), (5, 6)]
occurrences = {}
for tpl in tuple_list:
    if tpl in occurrences:
        occurrences[tpl] += 1
    else:
        occurrences[tpl] = 1
print(occurrences)
