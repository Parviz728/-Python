class PropertyDescriptor:
    def __init__(self, getter=None, setter=None, deleter=None):
        """
        Вызывается при обращении к декоратору
        
        :param getter: это та самая функция которая попадает под декоратор
        :type getter: function
        
        :param setter: это та самая функция которая попадает под декоратор
        :type setter: function
        
        :param deletter: это та самая функция которая попадает под декоратор
        :type deletter: function
        
        :return: Any
        """
        self.getter = getter
        self.setter = setter
        self.deleter = deleter

    def __get__(self, obj, type):
        """
        Вызывается при попытке получить значение атрибута класса PropertyDescriptor
        
        :param obj: ссылается на объект класса MyClass
        :type obj: MyClass
        
        :return: str
        """
        if obj is None:
            return self
        return self.getter(obj)
    
    def __set__(self, obj, value):
        """
        Вызывается при попытке присвоить значение атрибуту класса MyClass
        
        :param obj: ссылается на объект класса MyClass
        :type obj: MyClass
        
        :param value: присваиваемое значение
        :type value: Any
        
        :return: str
        """
        self.setter(obj, value)

    def __delete__(self, obj):
        """
        Вызывается при попытке удалить значение атрибута класса MyClass
        
        :param instance: ссылается на объект класса MyClass
        :type instance: MyClass
        
        :return: str
        """
        self.deleter(obj)
        
    
class MyClass:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        """
        геттер
        
        :param self: ссылается на объект класса MyClass
        :type self: MyClass
        
        :return: Any
        """
        return self._value

    def set_value(self, new_value):
        """
        Сеттер
        
        :param self: ссылается на объект класса MyClass
        :type self: MyClass
        
        :return: None
        """
        self._value = new_value
        
    def del_value(self):
        """
        делитер
        
        :param self: ссылается на объект класса MyClass
        :type self: MyClass
        
        :return: None
        """
        del self._value
        
    value = PropertyDescriptor(getter=get_value, setter=set_value, deleter=del_value) # а вот и сам декоратор

# Использование PropertyDescriptor в качестве декоратора
obj = MyClass(42)
print(obj.value)  # Получение значения. 42
obj.value = 100    # Установка значения
print(obj.value) # 100
print(obj.__dict__) # {'_value': 100}
del obj.value
print(obj.__dict__) # {}
