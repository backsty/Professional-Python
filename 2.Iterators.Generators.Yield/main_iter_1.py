class FlatIterator:
    def __init__(self, list_of_list):
        """
        Инициализируем сам итератор. Он принимает на вход список списков и сохраняет его в self.list_of_list
        и self.inner_index как 0. Эти индексы используются для отслеживания текущего списка и текущего списка и
        текущего элемента в текущем списке, которые должны быть возвращены.
        """
        self.list_of_list = list_of_list
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self):
        """
        Возвращает сам итератор. Это нужно для того, чтобы объект мог быть использован в списке.
        """
        return self

    def __next__(self):
        """
        Этот метод возвращает следующий элемент списка списков. Он использует self.outer_index для отслеживания текущего
        списка и self.inner_index для отслеживания текущего элемента в текущем списке. Когда все элементы в текущем
        списке были возвращен, self.outer_index увеличивается, чтобы перейти к следующему списку, и self.inner_index
        сбрасывается до 0. Если все списки были обработаны, метод вызывает StopIteration, чтобы сигнализировать, что все
        элементы были возвращены.
        """

        # if self.main_listed_cursor == len(self.list_of_list):
        #     raise StopIteration
        # else:
        #     len_iteration_list = len(self.list_of_list[self.main_listed_cursor])
        #     if self.nested_cursor < len_iteration_list - 1:
        #         self.nested_cursor += 1
        #         return self.list_of_list[self.main_listed_cursor][self.nested_cursor]
        #     else:
        #         self.main_listed_cursor += 1
        #         self.nested_cursor = -1
        #         # return self.__next__
        # return self.list_of_list[self.main_listed_cursor][self.nested_cursor]

        while self.outer_index < len(self.list_of_list):
            while self.inner_index < len(self.list_of_list[self.outer_index]):
                item = self.list_of_list[self.outer_index][self.inner_index]
                self.inner_index += 1
                return item
            self.outer_index += 1
            self.inner_index = 0
        raise StopIteration


def test_1():
    """
    Создаёт список списков и проверяет, что latIterator возвращает правильные элементы в правильном порядке. Она делает
    это, сравнивая каждый элемент, возвращаемый FlatIterator, с ожидаемым элементом, и проверяя, что список всех
    элементов, возвращаемых FlatIterator, равен ожидаемому списку элементов.
    """
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        print(f"flat: {flat_iterator_item}, check: {check_item}")
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()