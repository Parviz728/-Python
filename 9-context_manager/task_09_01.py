import datetime

class ErrorLoggerContextManager:
    def __init__(self, error_log_file):
        """
        Вызывается при создании экземпляра класса

        :param error_log_file: файл куда запихаем все логи ошибки
        :type error_log_file: file

        :return: None
        """
        self.error_log_file = error_log_file

    def __enter__(self):
        """
        Вызывается при входе в менеджер контекста

        :return: ErrorLoggerContextManager
        """
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """
        Вызывается при выходе из менеджера контекста

        :param exc_type: тип вызываемомго исключения
        :type exc_type: <class 'type'>

        :param exc_value: значение исключения
        :type exc_value: <class 'ZeroDivisionError'>

        :param exc_tb: адрес памяти
        :type exc_tb: <class 'traceback'>

        :return: bool
        """
        if exc_type is not None: # если возникла ошибка
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.error_log_file, 'w') as f:
                f.write(f"Error at {timestamp}:\n")
                f.write(f"Exception Type: {exc_type}\n")
                f.write(f"Exception Value: {exc_value}\n")
                f.write(f"Traceback: {exc_tb}\n")
            return False  # Прокидываем ошибку выше

with ErrorLoggerContextManager("error_log.txt"):
    result = 1 / 0