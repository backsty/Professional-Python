class TemplateIterator:
    def __init__(self):
        pass

    def __iter__(self):
        # Выполняется на входе в цикл

        return self

    def __next__(self):
        # Выполняется на каждой итерации цикла

        if ...:  # Условие завершения цикла
            raise StopIteration
        return  # Будеь подставляться в item
