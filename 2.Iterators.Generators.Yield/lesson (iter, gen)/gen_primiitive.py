def foo():

    for i in range(3):
        yield "1"
        yield "2"
        yield {}


data = foo()

for item in data:
    print(item)
