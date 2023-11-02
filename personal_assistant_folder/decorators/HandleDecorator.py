from functools import wraps


class HandleDecorator:
    @staticmethod
    def handle_exception(func):
        """
        Декоратор для обработки исключений в функциях, выполняющих ввод.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except ValueError as e:
                print(e)

        return wrapper
