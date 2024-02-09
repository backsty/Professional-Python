class FlatIterator:

    def __init__(self, list_):
        self._stack = [iter(list_)]

    def __iter__(self):
        return self

    def __next__(self):
        while self._stack:
            try:
                item = next(self._stack[-1])
            except StopIteration:
                self._stack.pop()
                continue
            if not isinstance(item, list):
                return item
            self._stack.append(iter(item))
        raise StopIteration


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
