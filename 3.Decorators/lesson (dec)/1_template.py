from functools import wraps


def decorator_template(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):

        # действия до вызова исходной функции
        result = old_function(*args, **kwargs)
        # действия после вызова исходной функции

        return result

    return new_function


def parametrized_decorator_template(param1, param2, param3):

    def decorator(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            # param1, param2, param3 можно использовать внутри функции

            # действия до вызова исходной функции
            result = old_function(*args, **kwargs)
            # действия после вызова исходной функции

            return result

        return new_function

    return decorator
