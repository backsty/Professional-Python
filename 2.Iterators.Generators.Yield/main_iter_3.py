class FlatIterator:

    def __init__(self, list_):
        self._stack = [[list_, 0]]

    def __iter__(self):
        return self

    def __next__(self):
        while self._stack:
            list_, i = self._stack[-1]
            if i < len(list_):
                self._stack[-1][1] += 1
                if not isinstance(list_[i], list):
                    return list_[i]
                self._stack.append([list_[i], 0])
            else:
                self._stack.pop()
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
