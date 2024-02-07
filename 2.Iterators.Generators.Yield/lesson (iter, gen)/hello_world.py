class HelloWorld:
    def __init__(self, number_of_iterations):
        self.number_of_iterations = number_of_iterations

    def __iter__(self):
        # Выполняется на входе в цикл
        self.counter = 0
        return self

    def __next__(self):
        # Выполняется на каждой итерации цикла

        self.counter += 1

        if self.counter > self.number_of_iterations:  # Условие завершения цикла
            raise StopIteration
        return "Hello, World!"


hello_world = HelloWorld(5)

for item in hello_world:
    print(item)
