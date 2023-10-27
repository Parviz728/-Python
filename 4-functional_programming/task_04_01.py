# Необходимо написать фабрику декораторов (также декоратор).
# Фабрика (функция) принимает аргумент - функцию (lambda).
# Возвращает декоратор, который должен вызывать функцию (lambda) с аргументом - результатом декорируемого декоратора.
from functools import wraps
from types import FunctionType

def fabric(lambda_func):
    """
    Фабрика декоратор.

    Эта фабрика создает и возвращает декоратор на функцию repeat, которая, в свою очередь, 
    декорирует foo

    :param lambda_func: Функция (lambda).
    :type lambda_func: function.

    :return: Внешний декоратор.
    :rtype: function.
    """
    # func - это функция repeat
    def outer_decorator(func_referenced_to_repeat: FunctionType = None, **kwargs):
        def decorated(arg_gone_to_repeat: int) -> FunctionType:
            def decor(func_referenced_to_foo: FunctionType) -> FunctionType:
                @wraps(func_referenced_to_foo)
                def wrapper(*a, **kw):
                    if fabric.is_on:
                        result_of_repeat = func_referenced_to_repeat(arg_gone_to_repeat) # вот она функция, которая вернет то, что вернет repeat
                        func_referenced_to_RepeatWrapper = result_of_repeat(func_referenced_to_foo) # то что вернет нам foo
                        go_to_lambda = func_referenced_to_RepeatWrapper(*a, **kw)
                        return lambda_func(go_to_lambda)
                    return lambda_func(func_referenced_to_foo(*a, **kw))
                return wrapper
            return decor
        return decorated
    return outer_decorator


@fabric(lambda x: x ** 2)
def repeat(times: int):
    """
    Повторить вызов times раз, и вернуть среднее значение.

    Декорируемая функция, которая будет вызывать функцию fun указанное количество
    раз и возвращать среднее значение результатов.

    :param times: Количество раз, которое нужно вызвать функцию fun.
    :type times: int.

    :return: Декорируемая функция.
    :rtype: function.
    """
    # func - это функция на которую навешивается наш декоратор
    def decorate(func: FunctionType) -> FunctionType:
        @wraps(func)
        def wrapper(*args, **kwargs) -> float:
            avg: float = sum(func(*args, **kwargs) for _ in range(times)) / times
            return avg
        return wrapper
    return decorate

@repeat(3)
def foo(*args, **kwargs):
    """Функция которая работает... и все (может принимать на вход любые параметры)"""
    print("Foo called!")
    return 4 # К этому значению далее применяется lambda функция (аргумент для fabric)


fabric.is_on = True
fabric.off = lambda: fabric.__setattr__('is_on', False) # функция выключающая фабрику
fabric.on = lambda: fabric.__setattr__('is_on', True) # функция включающая фабрику

print("Первый вызов")
print(foo(1, 3, 5))
print()
print("Выключаем фабрику")
fabric.off()
print("Второй вызов")
print(foo(1, 3, 5))
print()
print("Включаем обратно")
fabric.on()
print("Третий вызов")
print(foo(1, 3, 5))



