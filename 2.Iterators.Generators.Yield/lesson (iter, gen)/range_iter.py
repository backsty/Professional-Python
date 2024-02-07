class RangeIterator:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # Выполняется на входе в цикл
        self.current_value = self.start - 1
        return self

    def __next__(self):
        # Выполняется на каждой итерации цикла
        self.current_value += 1

        if self.current_value >= self.end:  # Условие завершения цикла
            raise StopIteration
        return self.current_value  # Будеь подставляться в item


range_iter = RangeIterator(1, 5)
for item in range_iter:
    print(item)
