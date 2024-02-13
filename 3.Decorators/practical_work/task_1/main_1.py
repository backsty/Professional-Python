import os
from datetime import datetime
from functools import wraps


# Доработать декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл 'main.log' дату и
# время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Функция test_1 в коде
# ниже также должна отработать без ошибок.


def build_path(file_name):
    current_dir = os.getcwd()  # путь до корневой папки (3.Decorators)
    full_path = os.path.join(current_dir, file_name)  # путь до main.log
    return full_path


# Декоратор для логирования
def logger(file_name):
    def decorator(old_function):
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

            # !!!Файл каждый раз перезаписывается!!!
            # Это сделано для того чтобы не хранить прошлые логи
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(writing_to_file)

            return result
        return new_function
    return decorator


def test_1():
    path = 'main.log'
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

    assert os.path.exists(path), 'Файл main.log должен существовать'

    summarize(4.3, b=2.2)
    summarize(a=0, b=0)

    with open(path, 'r', encoding='utf-8') as log_file:
        log_file_content = log_file.read()

    assert 'summarize' in log_file_content, 'Должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()
