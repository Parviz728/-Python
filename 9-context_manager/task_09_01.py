import datetime

class ErrorLoggerContextManager:
    def __init__(self, error_log_file):
        self.error_log_file = error_log_file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
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