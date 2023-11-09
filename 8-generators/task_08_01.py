# Первое решение
def myzip(*args):
    """
    Функция аналог zip

    :param args: совокупность итерабельных объектов
    :type args: tuple

    :yield: Any
    """
    mx = len(max(args, key=len))
    for i in range(mx):
        for lst in args:
            if i < len(lst):
                yield lst[i]                
print(list(myzip(['A', 'B', 'C'], [1, 2, 3]))) # ['A', 1, 'B', 2, 'C', 3]
print(list(myzip('!', ['A', 'B', 'C', 'D'], range(1, 3)))) # ['!', 'A', 1, 'B', 2, 'C', 'D']

# Второе решение
my_zip = lambda *args: (tuple(item[i] for item in args if i < len(item)) for i in range(max(map(len, args))))
print(list(my_zip(['A', 'B', 'C'], [1, 2, 3]))) # [('A', 1), ('B', 2), ('C', 3)]
print(list(my_zip('!', ['A', 'B', 'C', 'D'], range(1, 3)))) # [('!', 'A', 1), ('B', 2), ('C',), ('D',)]
