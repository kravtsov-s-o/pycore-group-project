from functools import wraps
from helpers.Logger import MyLogger

logger = MyLogger()


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
                logger.error(str(e))

        return wrapper
