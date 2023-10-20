my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
count = 0
for item in my_list:
    if isinstance(item, tuple):
        break
    count += 1
print(count)
