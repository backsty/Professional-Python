from tools import printable, with_attempts


@printable
@with_attempts(attempts=3, time_sleep=1)
def summ(a, b):
    return a + b


@with_attempts(attempts=10, time_sleep=0)
def div(a, b):
    return a / b


@printable
class A:

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"{self.a}"


a = A("a")
