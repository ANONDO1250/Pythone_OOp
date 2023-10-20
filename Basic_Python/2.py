t = (2, 3, 4, 5)
product = [t[i] * t[i + 1] for i in range(len(t) - 1)]
print(product)
