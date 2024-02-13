import os
from functools import wraps
from datetime import datetime


def build_path(file_name):
    current_dir = os.getcwd()
    full_path = os.path.join(current_dir, file_name)
    return full_path


def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            date_func = datetime.now()
            result = old_function(*args, **kwargs)
            writing_to_file = (
                f"Дата вызова функции: {date_func.strftime('%d.%m.%Y')}\n"
                f"Время вызова функции: {date_func.strftime('%H:%M:%S.%f')}\n"
                f"Имя функции: {old_function.__name__}\n"
                f"Аргументы функции: {args} and {kwargs}\n"
                f"результат выполнения функции: {result}\n"
            )

            with open(path, "a", encoding='utf-8') as file:
                file.write(writing_to_file)

            return result
        return new_function
    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summarize(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summarize(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summarize(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path, 'r', encoding='utf-8') as log_file:
            log_file_content = log_file.read()

        assert 'summarize' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()
