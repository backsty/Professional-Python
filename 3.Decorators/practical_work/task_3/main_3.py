import os
from datetime import datetime
from functools import wraps


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

            with open(path, "a", encoding="utf-8") as file:
                file.write(writing_to_file)

            return result
        return new_function
    return __logger