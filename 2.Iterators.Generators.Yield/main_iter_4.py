class FlatIterator:

    def __init__(self, list_of_list):
        self.stack = []
        self.current_list = list_of_list
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.current_list):
            if self.stack:
                # На данном этапе мы дошли до конца списка,
                # выходим из него во внешний и "вспоминаем" состояние
                self.current_list, self.counter = self.stack.pop()
                return next(self)
            else:
                raise StopIteration

        item = self.current_list[self.counter]
        self.counter += 1
        if type(item) is not list:
            return item
        else:
            # Запоминаем текущее состояние
            self.stack.append((self.current_list, self.counter))
            # Входим во вложенный список он становиться текущим
            self.current_list = item
            self.counter = 0
            return next(self)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
        print(f"flat: {flat_iterator_item}, check: {check_item}")
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
