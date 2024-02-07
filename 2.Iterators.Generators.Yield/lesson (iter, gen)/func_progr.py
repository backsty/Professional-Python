data = [1, 2, 3, 4, 5]

result = set(map(lambda x: x**2, filter(lambda x: x < 3, data)))
