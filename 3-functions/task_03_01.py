container = {}

# добавление человека с его номером
def add_number(name, number):
    container[name] = number
    print("Номер успешно побавлен в список")

# вывести номер человека
def get_number(name):
    return f"Номер {name}а: {container[name]}" if name in container else f"Такого человека нет в списке"

# удалить человека из телефонной книжки
def del_number(name):
    if name in container:
        del container[name]
        return f"номер {name}а удален из списка"
    return f"номера человека {name} нет в списке" 

while True:
    inp = input('1. Добавить номер\n'
            '2. Вывести номер\n'
            '3. Удалить номер\n')
    if inp == "Добавить номер":
        name, number = input("Введите имя: "), input("Введите номер: ")
        add_number(name, number)
    elif inp == "Вывести номер":
        name = input("Введите имя человека: ")
        print(get_number(name))
    elif inp == "Удалить номер":
        name = input("Введите имя человека: ")
        print(del_number(name))
    elif inp == "Выход":
        break
