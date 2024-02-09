import types


def flat_generator(list_of_list):
    for sublist in list_of_list:
        if isinstance(sublist, list):
            # Рекурсивный вызов для обработки вложенных списков
            # yield from flat_generator(sublist)
            for item in flat_generator(sublist):
                yield item
        else:
            yield sublist


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item
        print(f"flat: {flat_iterator_item}, check: {check_item}")

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()