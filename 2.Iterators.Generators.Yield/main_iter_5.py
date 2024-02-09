class FlatIterator:

    def __init__(self, list_of_list):
        self.stack = []
        self.current_iterator = iter(list_of_list)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                item = next(self.current_iterator)
            except StopIteration:
                if self.stack:
                    # На данном этапе мы дошли до конца списка,
                    # выходим из него во внешний и "вспоминаем" состояние
                    self.current_iterator = self.stack.pop()
                    continue
                    # Можно ещё использовать next(self) т. к. по сути метод next из __next__ вызывает сам себя
                    # и чтобы полностью избавиться от рекурсии используем continue и оборачиваем это всё в while True:.
                else:
                    # Выходить выше некуда, значить дошли до конца внешнего списка, следовательно просто выбрасываем
                    # исключение StopIteration
                    raise StopIteration

            if type(item) is not list:
                return item
            else:
                self.stack.append(self.current_iterator)
                self.current_iterator = iter(item)
                continue  # next(self)


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
