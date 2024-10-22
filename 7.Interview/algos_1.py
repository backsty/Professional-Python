class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def brackets_balance(string: str) -> str:
    """
    Программа ожидает на вход строку со скобками. На выход сообщение:
    «Сбалансированно», если строка корректная, и «Несбалансированно»,
    если строка составлена неверно.
    @param string:
    @return:
    """
    s = Stack()
    for i in string:
        if i in "({[":
            s.push(i)
        elif i in ")}]":
            if s.is_empty():
                output = "Несбалансированно"
                return output
            if i == ")" and s.peek() != "(":
                output = "Несбалансированно"
                return output
            if i == "}" and s.peek() != "{":
                output = "Несбалансированно"
                return output
            if i == "]" and s.peek() != "[":
                output = "Несбалансированно"
                return output
            s.pop()
    if s.is_empty():
        output = "Сбалансированно"
    else:
        output = "Несбалансированно"
    return output


if __name__ == '__main__':
    print(brackets_balance("(((([{}])))))"))
    print(brackets_balance("[([])((([[[]]])))]{()}"))
    print(brackets_balance("{{[()]}}"))
    print(brackets_balance("}{}"))
    print(brackets_balance("{{[(])]}}"))
    print(brackets_balance("[[{())}]"))