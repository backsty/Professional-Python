import time
from functools import wraps


def printable(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):
        # действия до вызова исходной функции
        print(
            f"Вызывается функция {old_function.__name__} "
            f"с аргументами {args} и {kwargs}"
        )

        result = old_function(*args, **kwargs)

        print(f"Функция {old_function.__name__} вернула результат {result}")
        # действия после вызова исходной функции

        return result

    return new_function


def with_attempts(attempts, time_sleep):

    number_of_calls = 0
    number_of_errors = 0
    list_of_errors = []

    def decorator(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            nonlocal number_of_calls, number_of_errors
            for i in range(attempts):
                error = None
                try:
                    number_of_calls += 1
                    result = old_function(*args, **kwargs)
                    return result

                except Exception as e:
                    list_of_errors.append(e)
                    number_of_errors += 1
                    error = e
                    print(f"Попытка {i + 1} не удалась: {e}")
                    print(f"Общее количество ошибок: {number_of_errors}")
                    time.sleep(time_sleep)

            raise error

        return new_function

    return decorator
