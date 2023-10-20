tuple1 = (4, 6)
tuple2 = (1, 2)
result = tuple(x - y for x, y in zip(tuple1, tuple2))
print(result)
