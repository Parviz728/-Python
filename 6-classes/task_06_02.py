from abc import ABC

kurses = {"$": 1.2, "₽": 60, "€": 1}

class Course:
    """
    класс Дескриптор
    """
    @classmethod
    def convert(cls, value: str):
        """
        Метод класса который конвертирует переданную строку типа "2$" или "1.5$"
        в целое или вещественное числовое значение
        
        :param value: строка с валютой
        :type owner: str
        
        :return: int или float
        """
        
        value = value[:-1] # убирает значок валюты с конца строки
        if '.' in value: # число типа float
            value = float(value)
        else:
            value = int(value)
        return value
    
    def __set_name__(self, owner, name):
        """
        Магический метод который автоматически вызывается
        когда создается объект класса Course
        
        :param owner: ссылка на класс Currency
        :type owner: Currency
        
        :param name: имя задаваемое атрибуту
        :type name: str
        
        :return: None
        """
        self.name = "_" + name
        
    def __get__(self, instance, owner):
        """
        Вызывается при попытке получить значение атрибута course класса Currency или его подклассов
        
        :param instance: ссылается на объект класса Currency или его подкласса
        :type instance: Currency или его подкласс
        
        :param owner: ссылка на класс Currency или его подкласс
        :type owner: Currency или его подкласс
        
        :return: str
        """
        if not instance:
            return kurses
        if not hasattr(instance, self.name):
            setattr(instance, self.name, kurses)
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """
        Вызывается при инициализации класса Currency
        
        :param self: ссылается на объект класса Course
        :type self: Course
        
        :param instance: ссылается на объект класса Currency или его подкласс
        :type instance: Currency или его подкласс
        
        :param value: значение которое мы присваиваем
        :type value: str
        
        :return: str
        """
        kurses[value[-1]] = self.convert(value) 
        setattr(instance, self.name, kurses) # 1€ = 60 рублей, 1€ = 1.2$
        
class Currency(ABC):
    """
    Абстрактный класс для определния интерфейса
    
    """
    course = Course() # дескриптор данных
    
    def __new__(cls, *args, **kwargs):
        """
        Вызывается при создании объекта класса родителя или подкласса
        Если его не переопределить, то метод to будет работать неверно
        ему будет не хватать именнованных аргументов класса ABC
        
        :return: ссылку на возвращаемый объект
        """
        return super().__new__(cls)
    
    def __init__(self, amount):
        # здесь вызовется дескриптор, т.к у него приоритет выше чем у свойств атрибутов
        # В классе Currency образуется protected атрибут _course со значением amount
        self.amount = amount
        self.course = "1.2$" # устанавливаем initial значение одного Евро
        
    @staticmethod
    def __verify_value(value):
        if not isinstance(value, (Euro, Dollar, Ruble)):
            raise TypeError("Операнд должен быть объектом класса одной из валют")
        
    @staticmethod
    def __verify_operation(operation):
        if not isinstance(operation, (int, float)):
            raise TypeError("Операнд должен быть числом")
    
    def __str__(self):
        return f"{self.amount}{self.__class__.sign}" # при попытке получить self.course срабатывает геттер из дескриптора
    
    def to(self, name):
        """
        Конвертировать в другую валюту
        
        :param name: ссылается на объект одного из классов валют
        
        :return: класс валюты в которую конвертируем
        """
        return name((self.amount / self.course[self.__class__.sign]) * self.course[name.sign])
    
    def __add__(self, other):
        """
        Сложение двух объектов
        
        :param other: ссылается на объект класса валюты
        
        :return: класс валюты
        """
        self.__verify_value(other)
        return self.__class__(self.amount + other.to(self.__class__).amount)
    
    def __radd__(self, other): # левый операнд (other) является числом
        return self + self.__class__(other)
    
    def __sub__(self, other):
        """
        Вычитание двух объектов
        
        :param other: ссылается на объект класса валюты
        
        :return: класс валюты
        """
        self.__verify_value(other)
        return self.__class__(self.amount - other.to(self.__class__).amount)
    
    def __gt__(self, other):
        """
        Проверка на >
        
        :param other: ссылается на объект класса валюты
        
        :return: bool
        """
        self.__verify_value(other)
        return self.amount > other.to(self.__class__).amount
    
    def __ge__(self, other):
        """
        Проверка на >=
        
        :param other: ссылается на объект класса валюты
        
        :return: bool
        """
        self.__verify_value(other)
        return self.amount >= other.to(self.__class__).amount
    
    def __truediv__(self, number):
        """
        Деление на число
        
        :param other: ссылается на объект класса валюты
        
        :return: float
        """
        self.__verify_operation(number)
        return self.__class__(self.amount / number)
    
    def __mul__(self, number):
        """
        Умножение на число
        
        :param other: ссылается на объект класса валюты
        
        :return: int
        """
        self.__verify_operation(number)
        return self.__class__(self.amount * number)
    
class Euro(Currency):
    sign = "€"
    
class Dollar(Currency):
    sign = "$"
    
class Ruble(Currency):
    sign = "₽"
    
e = Euro(5)
print(e)
# 5€
print(e.to(Dollar))
# 6.0$
print(sum([Euro(i) for i in range(5)]))
# 10.0€
print(e > Euro(6))
# False
print(e + Dollar(10))
# 13.333333333333334€
print(Dollar(10) + e)
# 16.0$
e.course = "2$" # установили курс евро в два доллара, можно установить курс любой валюты
# 10.0$
print(Euro.course[Dollar.sign])
# 2
print(Euro.course[Ruble.sign])
# 60
print(e.sign)
# €
